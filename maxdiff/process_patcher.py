from freezing_utils import get_patcher_dict


class Processor:
    def process_elements(self, patcher, voice_count: int, abstraction_name=""):
        """Processes patchers."""

    def get_results(self):
        """Returns the current results."""
        return None


def process_patch(patcher, abstraction_entries: list[dict], processor: Processor):
    process_patch_recursive(patcher, abstraction_entries, processor, 1, "")


def process_patch_recursive(
    patcher,
    abstraction_entries: list[dict],
    processor: Processor,
    voice_count: int,
    abstraction_file_name: str,
):
    """Recursively progress through subpatchers, invoking the processor for every patcher
    inluding every instance of the patch's dependencies that can be found among the
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
            process_patch_recursive(patch, abstraction_entries, processor, 1, "")

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
        if patch == {}:
            continue  # something went wrong when parsing the abstraction

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
    abstraction_filenames = [str(item["file_name"]) for item in abstraction_entries]

    if "text" in box:
        if box["text"].startswith("poly~"):
            name = box["text"].split(" ")[1] + ".maxpat"
            if name in abstraction_filenames:
                return name
            else:
                raise ValueError(
                    "poly~ pointing to file that is not known as a dependency: " + name
                )
        else:
            name = box["text"].split(" ")[0] + ".maxpat"
            if name in abstraction_filenames:
                return name

    if box.get("maxclass") == "bpatcher" and box.get("embed") != 1:
        if box.get("name") in abstraction_filenames:
            return box["name"]
        else:
            raise ValueError(
                "Non-embedded bpatcher pointing to file that is not known as a dependency: "
                + box["name"]
            )

    return None
