import json
from freezing_utils import device_entry_with_data
from collections import Counter


class Processor:
    def process_elements(self, patcher, voice_count: int, abstraction_name=""):
        """Processes patchers."""

    def get_results(self):
        """Returns the current counts."""
        return None


def get_stats(entries: list[device_entry_with_data]):
    """Returns statistics for this device"""

    device = entries[0]  # the first entry is always the device file

    abstraction_entries = [
        item for item in entries if str(item["file_name"]).endswith(".maxpat")
    ]

    device_patch = get_patcher_dict(device)
    count_processor = CountProcessor()
    process_patch_recursive(
        device_patch,
        abstraction_entries,
        count_processor,  # do recurse into abstractions
    )

    object_count_recursive, line_count_recursive = count_processor.get_results()

    summary = "\n"
    summary += "Total - Counting every abstraction instance - Indicates loading time\n"
    summary += f"    Object instances: {object_count_recursive}\n"
    summary += f"    Connections: {line_count_recursive}\n"

    object_count_once = 0
    line_count_once = 0
    for entry in entries:
        if entry["type"] != "JSON":
            continue

        entry_patch = get_patcher_dict(entry)
        count_processor = CountProcessor()
        # don't recurse into abstractions
        process_patch_recursive(entry_patch, [], count_processor)
        o, l = count_processor.get_results()
        object_count_once += o
        line_count_once += l

    summary += "Unique - Counting abstractions once - Indicates maintainability\n"
    summary += f"    Object instances: {object_count_once}\n"
    summary += f"    Connections: {line_count_once}\n"

    return summary


def get_used_abstractions(entries: list[device_entry_with_data]) -> dict[str, int]:
    device = entries[0]  # the first entry is always the device file

    abstraction_entries = [
        item for item in entries if str(item["file_name"]).endswith(".maxpat")
    ]

    device_patch = get_patcher_dict(device)
    abstractions_processor = AbstractionFileNamesProcessor()
    process_patch_recursive(device_patch, abstraction_entries, abstractions_processor)
    return abstractions_processor.get_results()


def process_patch_recursive(
    patcher,
    abstraction_entries: list[dict],
    processor: Processor,
    voice_count: int = 1,
    abstraction_file_name: str = "",
):
    """Recursively progress through subpatchers, invoking the processor for every patcher
    Inluding every instance of the patch's dependencies that can be found among the
    abstraction files that were passed in.

    Arguments
    patcher: patcher to process
    abstraction_entries: list of abstraction entries in frozen device
    processor: instance of a Processor that is invoked for this patch
    voice_count: the amount of voices when this patcher occurs in a poly~ in its parent patch
    abstraction_file_name: the file name of the abstraction this patch is in, if it is in an abstraction
    """
    processor.process_elements(patcher, voice_count, abstraction_file_name)

    for box_entry in patcher["boxes"]:
        box = box_entry["box"]

        if "patcher" in box and (
            box.get("maxclass") != "bpatcher" or box.get("embed") == 1
        ):
            patch = box["patcher"]
            # get subpatcher or embedded bpatcher count
            process_patch_recursive(patch, abstraction_entries, processor)

        # if no abstractions were passed in, we assume we don't want to recurse into abstarctions
        if len(abstraction_entries) == 0:
            continue

        # check for known abstraction
        file_name = get_abstraction_name(box, abstraction_entries)
        if file_name is None:
            continue

        abstraction = [
            item for item in abstraction_entries if item["file_name"] == file_name
        ][0]
        patch = get_patcher_dict(abstraction)

        voice_count = 1
        if "text" in box and box["text"].startswith("poly~"):
            # get poly abstraction count
            tokens = box["text"].split(" ")
            voice_count = int(tokens[2]) if len(tokens) > 2 else 1

        process_patch_recursive(
            patch,
            abstraction_entries,
            processor,
            voice_count,
            file_name,
        )


def get_abstraction_name(box, abstraction_entries: list[dict]):
    """
    Checks if this box is an abstraction and if so, return the name of the abstraction file.
    - returns None if this is not an abstraction
    - throws error if an abstraction name was expected but it was not found in the list of known names
    """
    # cache names of known abstractions. TODO: find a way to do this more efficiently.
    abstraction_file_names = [str(item["file_name"]) for item in abstraction_entries]

    if "text" in box:
        if box["text"].startswith("poly~"):
            name = box["text"].split(" ")[1] + ".maxpat"
            if name in abstraction_file_names:
                return name
            else:
                raise ValueError(
                    "poly~ pointing to file that is not known as a dependency: " + name
                )
        else:
            name = box["text"].split(" ")[0] + ".maxpat"
            if name in abstraction_file_names:
                return name

    if box.get("maxclass") == "bpatcher" and box.get("embed") != 1:
        if box.get("name") in abstraction_file_names:
            return box["name"]
        else:
            raise ValueError(
                "Non-embedded bpatcher pointing to file that is not known as a dependency: "
                + box["name"]
            )

    return None


def get_patcher_dict(entry: device_entry_with_data):
    """Returns the dict that represents the given patcher data.
    Prints errors if parsing fails"""

    if not "data" in entry:
        return {}

    patch_data = entry["data"]
    if not isinstance(patch_data, bytes):
        return {}

    if not "file_name" in entry:
        return {}

    name = entry["file_name"]
    if not isinstance(name, str):
        return {}

    device_data_text = ""
    try:
        if patch_data[len(patch_data) - 1] == 0:
            device_data_text = patch_data[: len(patch_data) - 1].decode("utf-8")
        else:
            device_data_text = patch_data.decode("utf-8")
    except Exception as e:
        print(f"Error getting patch data as text for entry {name}: {e}")
        return {}

    try:
        patcher_dict = json.loads(device_data_text)
    except ValueError as e:
        print(f"Error parsing device patch data as json for entry {name}: {e}")
        return {}

    try:
        patcher = patcher_dict["patcher"]
        return patcher
    except:
        print(f"Content of entry {name} does not seem to be a patcher")
        return {}


class CountProcessor(Processor):
    def __init__(self):
        self.object_count = 0
        self.line_count = 0

    def process_elements(self, patcher, voice_count: int, abstraction_name=""):
        """Counts objects and lines in the given patcher."""
        self.object_count += len(patcher.get("boxes", [])) * voice_count
        self.line_count += len(patcher.get("lines", [])) * voice_count

    def get_results(self):
        """Returns the current counts."""
        return self.object_count, self.line_count


# TODO: expend with dependencies that might be included in the frozen device, like pictures
class AbstractionFileNamesProcessor(Processor):
    def __init__(self):
        self.found_abstractions = {}

    def process_elements(self, patcher, voice_count: int, abstraction_name=""):
        """If this patcher is an abstraction, i.e. when an abstraction_name is passed in, increment the entry in the dict"""
        if abstraction_name != "":
            if abstraction_name in self.found_abstractions:
                self.found_abstractions[abstraction_name] += voice_count
            else:
                self.found_abstractions[abstraction_name] = voice_count

    def get_results(self):
        """Returns a dict of used abstractions mapped to how oftern they are used."""
        return self.found_abstractions
