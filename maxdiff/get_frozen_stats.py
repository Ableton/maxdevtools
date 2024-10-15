import json
from freezing_utils import device_entry_with_data


def get_frozen_stats(entries: list[device_entry_with_data]):
    """Returns statistics for this device"""

    device_data = entries[0]["data"]  # the first entry is always the device file

    abstractions = [
        item for item in entries if str(item["file_name"]).endswith(".maxpat")
    ]

    # cache names of known abstractions
    file_names = [str(item["file_name"]) for item in abstractions]

    patch = get_patcher_dict(device_data)
    object_count = count_objects(patch, abstractions, file_names)

    summary = "\n"
    summary += "Total - Counting every abstraction instance - Indicates loading time\n"
    summary += f"    Object instances: {object_count}\n"
    summary += "    Connections:\n"
    summary += "Unique - Counting abstractions once - Indicates maintainability\n"
    summary += "    Object instances:\n"
    summary += "    Connections:\n"
    return summary


def count_objects(patcher, entries: list[dict], file_names: list[str]):
    """Recursively counts all object instances in this patcher,
    inluding in every instance of its dependencies"""
    boxes = patcher["boxes"]
    count = 0
    for box_entry in boxes:
        box = box_entry["box"]
        count += 1

        if "patcher" in box:
            patch = box["patcher"]
            if box.get("maxclass") == "bpatcher" and box.get("embed") == 1:
                # get embedded bpatcher count
                count += count_objects(patch, entries, file_names)
            else:
                # get subpatcher count
                count += count_objects(patch, entries, file_names)
        else:
            abstraction_name = get_abstraction_name(box, file_names)
            if abstraction_name is None:
                continue

            abstraction = [
                item for item in entries if item["file_name"] == abstraction_name
            ][0]
            abstraction_data = abstraction["data"]
            abstraction_patch = get_patcher_dict(abstraction_data)
            abstraction_count = count_objects(abstraction_patch, entries, file_names)

            if "text" in box and box["text"].startswith("poly~"):
                # get poly abstraction count
                voice_count = int(box["text"].split(" ")[2])
                count += abstraction_count * voice_count
            else:
                # get abstraction count
                count += abstraction_count

    return count


def get_abstraction_name(box, file_names: list[str]):
    """
    Checks if this box is an abstraction and if so, return the name of the abstraction file.
    - returns None if this is not an abstraction
    - throws error if an abstraction name was expected but it was not found in the list of known names
    """
    if "text" in box:
        if box["text"].startswith("poly~"):
            name = box["text"].split(" ")[1] + ".maxpat"
            if name in file_names:
                return name
            else:
                raise ValueError(
                    "poly~ pointing to file that is not known as a dependency: " + name
                )
        else:
            name = box["text"].split(" ")[0] + ".maxpat"
            if name in file_names:
                return name

    if box.get("maxclass") == "bpatcher" and box.get("embed") != 1:
        if box.get("name") in file_names:
            return box["name"]
        else:
            raise ValueError(
                "Non-embedded bpatcher pointing to file that is not known as a dependency: "
                + box["name"]
            )

    return None


def get_patcher_dict(patch_data):
    """Returns the dict that represents the given patcher data.
    Prints errors if parsing fails"""
    device_data_text = ""

    try:
        if patch_data[len(patch_data) - 1] == 0:
            device_data_text = patch_data[: len(patch_data) - 1].decode("utf-8")
        else:
            device_data_text = patch_data.decode("utf-8")
    except Exception as e:
        print(f"Error getting device patch data as text: {e}")

    if device_data_text == "":
        print("Device has no data")

    patcher_dict = {}
    try:
        patcher_dict = json.loads(device_data_text)
    except ValueError as e:
        print(f"Error parsing device patch data as json: {e}")

    if not "patcher" in patcher_dict:
        print("Device content does not seem to be a patcher")

    return patcher_dict["patcher"]
