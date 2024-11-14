import json
from freezing_utils import device_entry_with_data


def get_frozen_stats(entries: list[device_entry_with_data]):
    """Returns statistics for this device"""

    device = entries[0]  # the first entry is always the device file

    abstraction_entries = [
        item for item in entries if str(item["file_name"]).endswith(".maxpat")
    ]

    # cache names of known abstractions
    abstraction_filenames = [str(item["file_name"]) for item in abstraction_entries]

    device_patch = get_patcher_dict(device)
    object_count_recursive, line_count_recursive = count(
        device_patch,
        abstraction_entries,
        abstraction_filenames,  # do recurse into abstractions
    )

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
        o, l = count(entry_patch, [], [])  # don't recurse into abstractions
        object_count_once += o
        line_count_once += l

    summary += "Unique - Counting abstractions once - Indicates maintainability\n"
    summary += f"    Object instances: {object_count_once}\n"
    summary += f"    Connections: {line_count_once}\n"

    return summary


def count(
    patcher, abstractions: list[dict], abstraction_filenames: list[str]
) -> tuple[int, int]:
    """Recursively counts all object instances and connections in this patcher,
    inluding in every instance of its dependencies that can be found among the
    files that were passed in"""
    boxes = patcher["boxes"]
    lines = patcher["lines"]
    object_count = len(boxes)
    line_count = len(lines)

    for box_entry in boxes:
        box = box_entry["box"]

        if "patcher" in box:
            patch = box["patcher"]
            if box.get("maxclass") != "bpatcher" or (
                box.get("maxclass") == "bpatcher" and box.get("embed") == 1
            ):
                # get subpatcher or embedded bpatcher count
                o, l = count(patch, abstractions, abstraction_filenames)
                object_count += o
                line_count += l

    if len(abstraction_filenames) == 0:
        return (object_count, line_count)

    # recurse into abstractions
    for box_entry in boxes:
        box = box_entry["box"]

        file_name = get_abstraction_name(box, abstraction_filenames)
        if file_name is None:
            continue

        abstraction = [item for item in abstractions if item["file_name"] == file_name][0]
        abstraction_patch = get_patcher_dict(abstraction)
        o, l = count(abstraction_patch, abstractions, abstraction_filenames)

        if "text" in box and box["text"].startswith("poly~"):
            # get poly abstraction count
            tokens = box["text"].split(" ")
            voice_count = int(tokens[2]) if len(tokens) > 2 else 1
            object_count += o * voice_count
            line_count += l * voice_count
        else:
            # get abstraction count
            object_count += o
            line_count += l

    return (object_count, line_count)


def get_abstraction_name(box, abstraction_filenames: list[str]):
    """
    Checks if this box is an abstraction and if so, return the name of the abstraction file.
    - returns None if this is not an abstraction
    - throws error if an abstraction name was expected but it was not found in the list of known names
    """
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
