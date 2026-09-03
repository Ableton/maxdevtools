from freezing_utils import device_entry_with_data, get_patcher_dict, get_external_name
from process_patcher import PatcherProcessor, walk_patch


def get_frozen_stats(entries: list[device_entry_with_data]) -> tuple[int, int, int, int]:
    """Returns statistics for the passed list of entries found in a frozen device"""

    device = entries[0]  # the first entry is always the device file

    abstraction_entries = [
        item for item in entries if str(item["file_name"]).endswith(".maxpat")
    ]

    device_patch = get_patcher_dict(device)
    if device_patch == {}:
        return 0, 0, 0, 0

    # get total counts: parse every instance of every abstraction
    count_processor = CountProcessor()
    walk_patch(
        device_patch, abstraction_entries, count_processor  # do recurse into abstractions
    )
    object_count_total, line_count_total = count_processor.get_results()

    # get unique counts: parse every entry included in the frozen device once
    object_count_unique = 0
    line_count_unique = 0
    for entry in entries:
        filename = str(entry["file_name"])
        if not (filename.endswith(".amxd") or filename.endswith(".maxpat")):
            continue

        entry_patch = get_patcher_dict(entry)
        if entry_patch == {}:
            continue

        count_processor = CountProcessor()
        walk_patch(entry_patch, [], count_processor)  # don't recurse into abstractions
        o, l = count_processor.get_results()

        object_count_unique += o
        line_count_unique += l

    return object_count_total, line_count_total, object_count_unique, line_count_unique


class CountProcessor(PatcherProcessor):
    def __init__(self):
        self.object_count = 0
        self.line_count = 0

    def process_patcher(self, patcher, poly_voice_count: int, abstraction_name=""):
        """Counts objects and lines in the given patcher."""
        self.object_count += len(patcher.get("boxes", [])) * poly_voice_count
        self.line_count += len(patcher.get("lines", [])) * poly_voice_count

    def get_results(self):
        """Returns the current counts."""
        return self.object_count, self.line_count


def get_frozen_file_usage(entries: list[device_entry_with_data]) -> dict[str, int]:
    """Returns a dict with the names of all the files that are frozen into this device
    with how often they are used in the device.

    It does this by parsing the top patcher and the abstractions found in `entries` recursively
    and finding how many objects match with the file names of the bundled dependencies.

    Externals are included in the dict just by name. These names can be matched later with
    the actual bundled external files.
    """
    device = entries[0]  # the first entry is always the device file

    abstraction_entries = [
        item for item in entries if str(item["file_name"]).endswith(".maxpat")
    ]

    external_names = list(
        dict.fromkeys(
            get_external_name(item["file_name"])
            for item in entries
            if get_external_name(item["file_name"]) != ""
        )
    )

    device_patch = get_patcher_dict(device)
    if device_patch == {}:
        return {}

    dependency_file_names_processor = DependencyUsageCounter(external_names)
    walk_patch(device_patch, abstraction_entries, dependency_file_names_processor)
    return dependency_file_names_processor.get_results()


class DependencyUsageCounter(PatcherProcessor):
    def __init__(self, external_names):
        self.external_names = external_names
        self.filename_occurrences = {}

    def process_patcher(self, patcher, poly_voice_count: int, abstraction_name=""):
        """If this patcher is an abstraction, i.e. when an abstraction_name is passed in, increment the entry in the dict.
        For other patchers, scan them for objects that use files.
        """

        filenames = get_dependency_filenames(patcher)
        filenames.extend(get_externals(patcher, self.external_names))
        if abstraction_name != "":
            filenames.append(abstraction_name)

        for filename in filenames:
            if filename in self.filename_occurrences:
                self.filename_occurrences[filename] += poly_voice_count
            else:
                self.filename_occurrences[filename] = poly_voice_count

    def get_results(self):
        """Returns a dict of used abstractions mapped to how often they are used."""
        return self.filename_occurrences


def get_externals(patcher, external_names):
    """Check all boxes in this patcher (don't recurse into subpatchers) and collect any objects that are externals"""
    externals = []
    for box_entry in patcher["boxes"]:
        box = box_entry["box"]
        object_type = box["maxclass"]
        if object_type == "newobj":
            if "text" in box:
                boxtext = box["text"]
                object_name = boxtext.split(" ")[0]
                if object_name in external_names:
                    externals.append(object_name)
    return externals


def get_dependency_filenames(patcher):
    """Check all boxes in this patcher (don't recurse into subpatchers) and collect any dependencies they might be referring to"""
    filenames = []
    for box_entry in patcher["boxes"]:
        box = box_entry["box"]

        if box.get("pic"):  # fic
            filenames.append(box.get("pic"))
            continue

        if box.get("pictures"):  # live.text, live.tab and live.menu
            for name in box.get("pictures"):
                filenames.append(name)
            continue

        if box.get("maxclass") == "pictctrl":
            if box.get("name"):
                filenames.append(box.get("name"))
            continue

        if box.get("bkgndpict"):  # pictslider and matrixctrl
            filenames.append(box.get("bkgndpict"))
            continue

        if box.get("knobpict"):  # pictslider
            filenames.append(box.get("knobpict"))
            continue

        if box.get("cellpict"):  # pictslider
            filenames.append(box.get("cellpict"))
            continue

        if box.get("filename"):  # jsui
            filenames.append(box.get("filename"))
            continue

        if box.get("filename"):  # jsui
            filenames.append(box.get("filename"))
            continue

        if box.get("text") and box.get("text").startswith("sfplay~"):  # sfplay~
            audiofile = get_max_attribute(box, "audiofile")
            if audiofile:
                filenames.append(audiofile)
                continue

        if box.get("text") and box.get("text").startswith("gen~"):  # gen~
            filename = get_max_attribute(box, "gen")
            if filename:
                filenames.append(add_if_needed(filename, ".gendsp"))
                continue

        if box.get("text") and (
            box.get("text").startswith("jit.gen") or box.get("text").startswith("jit.pix")
        ):  # jit.gen and jit.pix
            filename = get_max_attribute(box, "gen")
            if filename:
                filenames.append(add_if_needed(filename, ".genjit"))
                continue

        if box.get("text") and box.get("text").startswith("node.script"):  # node
            filename = box.get("text").split("node.script ")[1].split()[0]
            filenames.append(add_if_needed(filename, ".js"))

        if box.get("text") and box.get("text").startswith("pattrstorage"):  # pattrstorage
            filename = box.get("text").split("pattrstorage ")[1].split()[0]
            filenames.append(add_if_needed(filename, ".json"))
            continue

        if box.get("text") and box.get("text").startswith("table"):  # pattrstorage
            filename = box.get("text").split("table ")[1].split()[0]
            filenames.append(filename)
            continue

        if box.get("maxclass") == "playlist~" and box.get("data"):  # playlist~
            for clip in box["data"].get("clips"):
                if clip.get("filename"):
                    filenames.append(clip.get("filename"))
            continue

        if box.get("saved_object_attributes") and box["saved_object_attributes"].get(
            "filename"
        ):  # js
            filename = box["saved_object_attributes"].get("filename")
            filenames.append(add_if_needed(filename, ".js"))
            continue

    return filenames


def get_max_attribute(box, attribute_name: str):
    """parse the box text for a specific attribute value"""
    attrstring = "@" + attribute_name + " "
    if box.get("text") and attrstring in box.get("text"):
        return box.get("text").split(attrstring)[1].split()[0]
    return None


def add_if_needed(s: str, ext: str):
    """add an extension to a string if it doesn't exist yet"""
    return s + ext if not s.endswith(ext) else s
