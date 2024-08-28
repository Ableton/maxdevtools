from known_objects import known_objects

def get_num_inlets():
    max_inlets = 0
    max_inlet_name = "not found"

    max_outlets = 0
    max_outlet_name = "not found"

    for item in known_objects["boxes"]:
        # Access the 'box' dictionary
        box = item["box"]
        # Get the 'numinlets' value
        num_inlets = box["numinlets"]
        num_outlets = box["numoutlets"]
        box_text = get_box_text(box)
        if num_inlets > max_inlets:
            max_inlets = num_inlets
            max_inlet_name = box_text

        if num_outlets > max_outlets:
            max_outlets = num_outlets
            max_outlet_name = box_text

        print(f"Object: {box_text}, numinlets: {num_inlets}, numoutlets: {num_outlets}")

    print("------------------------------------------")
    print(f"Highest number of inlets: {max_inlets}, for {max_inlet_name}")
    print(f"Highest number of outlets: {max_outlets}, for {max_outlet_name}")

def get_box_text(box: dict) -> str:
    """Extract the text in a box in a Max patch.

    A box is otherwise known as an "object".
    """
    objecttype = box["maxclass"]
    boxtext = objecttype
    if objecttype == "newobj":
        if "text" in box:
            boxtext = box["text"]
        else:
            boxtext = "- empty -"
    elif "text" in box:
        boxtext = f"{objecttype} {box['text']}"

    if objecttype == "bpatcher" and "name" in box:
        boxtext = f"{boxtext} {box['name']}"

    return boxtext


def main():
    """Entry point of the program."""

    try:
        get_num_inlets()
    except RuntimeError:
        sys.exit(2)


if __name__ == "__main__":
    main()
