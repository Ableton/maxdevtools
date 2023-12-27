from known_objects import known_objects
from default_patcher import default_patcher
from object_aliases import object_aliases


def print_patcher(patcher_dict, summarize=True):
    """
    Prints a summary of a patcher dict.
    Note that the script should only format properties it knows about or is actively set to skip.
    Unknown or unexpected data should always be printed as raw json, so that the summary never discards valuable information.
    """
    if summarize:
        known_objects_map = {}
        for box_obj in known_objects["boxes"]:
            box = box_obj["box"]
            name = get_box_text(box)
            known_objects_map[name] = box

        return print_patcher_summary_recursive(patcher_dict, known_objects_map)
    else:
        import json

        return json.dumps(patcher_dict, indent=4, sort_keys=True)


def print_patcher_summary_recursive(patcher_dict, known_objects_map, indent=0):
    if (
        "patcher" not in patcher_dict
        or "boxes" not in patcher_dict["patcher"]
        or "lines" not in patcher_dict["patcher"]
    ):
        return ""

    summary_string = ""

    patcher = patcher_dict["patcher"]

    #### patcher ####

    skip_patcher_properties = [
        "boxes",  # iterated over later
        "lines",  # iterated over later
        "parameters",  # treated separately
        "dependency_cache",  # treated separately
        "project",  # treated separately
        "styles",  # treated separately
    ]

    properties = get_properties_to_print(patcher, default_patcher, skip_patcher_properties)

    display_text = ""
    for key, value in properties.items():
        if key == "appversion":
            display_text += get_appversion_string_short(value)
            continue

        display_text = concat(display_text, key + ": " + get_property_string(value))

    if "parameters" in patcher:
        display_text += get_parameters_string_block(patcher["parameters"])

    if "dependency_cache" in patcher:
        display_text += get_dependency_cache_string_block(patcher["dependency_cache"])

    if "project" in patcher:
        display_text += get_project_string_block(patcher["project"])

    if "styles" in patcher:
        display_text += get_styles_string_block(patcher["styles"], indent)

    if display_text != "":
        summary_string += ("\t") * indent + display_text + "\n"

    #### objects ####

    if not patcher["boxes"]:
        return

    summary_string += ("\t") * indent + "----------- objects -----------" + "\n"

    # every entry of "boxes" has a single item "box"
    boxes = list(map(lambda val: val["box"], patcher["boxes"]))

    skip_box_properties = [
        "maxclass",  # used in box name
        "text",  # shown in box name
        "id",  # used only for lines
        "name",  # shown in box name
        "patching_rect",  # different every time
        "numinlets",  # cached from inlet objects
        "numoutlets",  # cached from outlet objects
        "outlettype",  # cached from outlet objects
        "patcher",  # treated separately
        "locked_bgcolor",  # duplicate from patcher properties
        "editing_bgcolor",  # duplicate from patcher properties
        "color",  # duplicate from patcher properties
    ]

    ids_to_names = {}
    for box in boxes:
        box_text = get_box_text(box)

        ids_to_names[box["id"]] = box_text

        display_text = ""
        object_name = box_text.split()[0]

        if object_name not in known_objects_map and object_name in object_aliases:
            object_name = object_aliases[object_name]

        default_box = {}
        if object_name in known_objects_map:
            default_box = known_objects_map[object_name]

        properties = get_properties_to_print(box, default_box, skip_box_properties)

        for key, value in properties.items():
            if key == "code":
                display_text += get_code_string_block(value, indent + 1)
                continue

            display_text = concat(display_text, key + ": " + get_property_string(value))

        summary_string += ("\t") * indent + "[" + box_text + "] " + display_text + "\n"

        if "patcher" in box:
            summary_string += print_patcher_summary_recursive(
                box, known_objects_map, indent + 1
            )

    #### patch cords ####

    if len(patcher["lines"]) == 0:
        return summary_string

    summary_string += ("\t") * indent + "----------- patch cords -----------" + "\n"

    lines = []
    for val in patcher_dict["patcher"]["lines"]:
        lines.append(val["patchline"])

    def line_sort(line):
        return ids_to_names[line["source"][0]]

    lines.sort(key=line_sort)

    # We don't try to vertically align the sources and destinations of the lines,
    # even though that might make this more readable; a change in the maximum
    # source object length would affect all other printed lines

    for line in lines:
        from_name = "[" + ids_to_names[line["source"][0]] + "]"
        from_outlet = "(" + str(line["source"][1]) + ")"
        to_name = "[" + ids_to_names[line["destination"][0]] + "]"
        to_inlet = "(" + str(line["destination"][1]) + ")"

        display_text = from_name + " " + from_outlet + " => " + to_inlet + " " + to_name
        summary_string += ("\t") * indent + display_text + "\n"

    return summary_string


def get_box_text(box):
    objecttype = box["maxclass"]
    boxtext = objecttype
    if objecttype == "newobj":
        boxtext = box["text"]
    elif "text" in box:
        boxtext = objecttype + " " + box["text"]

    if objecttype == "bpatcher" and "name" in box:
        boxtext = boxtext + " " + box["name"]

    return boxtext


def get_properties_to_print(box_or_patcher, default, skip_properties):
    properties = {}
    for key, value in box_or_patcher.items():
        if key in skip_properties:
            continue

        if key in default and default[key] == value:
            continue

        if value == "":
            # TODO: are we sure there are no properties that have default values of some string but can be set to an empty string?
            continue

        if key == "saved_attribute_attributes":
            # We take the attributes out or saved_attribute_attributes and present them as properties
            attributes = get_saved_attribute_attributes(value)
            attributes_to_print = get_properties_to_print(attributes, default, skip_properties)
            for new_key, new_value in attributes_to_print.items():
                properties[
                    new_key
                ] = new_value  # this may overwrite existing value-based colors. This is ok, we want dynamic color values instead.
            continue

        if key == "saved_object_attributes":
            # We take the attributes out or saved_object_attributes and present them as properties
            attributes = get_saved_object_attributes(value)
            attributes_to_print = get_properties_to_print(attributes, default, skip_properties)
            for new_key, new_value in attributes_to_print.items():
                properties[new_key] = new_value
            continue

        if key not in properties:
            # Don't overwrite existing dynamic colors
            properties[key] = value

    return properties


def get_property_string(value):
    if isinstance(value, list):
        property_string = ""
        for item in value:
            if property_string != "":
                property_string += ", "

            if isinstance(item, float):
                if item.is_integer():
                    property_string += "{:.0f}".format(item)
                else:
                    property_string += "{:.2f}".format(item)
            else:
                property_string += str(item)
        return "[" + property_string + "]"

    return str(value)


def get_code_string_block(value, indent_amount):
    return "\n" + indent(value, indent_amount)


def get_saved_attribute_attributes(value):
    result = {}
    for attrkey, attrvalue in value.items():
        if attrvalue == "":
            continue

        if attrkey == "valueof":
            # Handle parameter info. TODO: are there usages of valueof other than for parameter info?
            result["parameter"] = "<" + getObjectParameterString(attrvalue) + ">"
            continue

        # Handle dynamic colors
        if "expression" in attrvalue:
            if attrvalue["expression"] == "":
                continue

            if attrvalue["expression"].startswith("themecolor."):
                result[attrkey] = attrvalue["expression"].split(".")[1]
                continue

        result[attrkey] = attrvalue
    return result


def get_saved_object_attributes(value):
    result = {}
    for attrkey, attrvalue in value.items():
        if attrvalue == "":
            continue

        result[attrkey] = attrvalue
    return result


def get_parameters_string_block(parameters):
    parameters_string = ""
    for key, value in parameters.items():
        if key in ["parameter_overrides", "parameterbanks"]:
            continue

        if (
            "parameter_overrides" in parameters
            and key in parameters["parameter_overrides"]
        ):

            override = parameters["parameter_overrides"][key]
            override_print = []
            override_print.append(
                override["parameter_longname"]
                if ("parameter_longname" in override)
                else "-"
            )
            override_print.append(
                override["parameter_shortname"]
                if ("parameter_shortname" in override)
                else "-"
            )
            override_print.append(
                str(override["parameter_linknames"])
                if ("parameter_linknames" in override)
                else "-"
            )

            for key2, value2 in override.items():
                if key2 in [
                    "parameter_longname",
                    "parameter_shortname",
                    "parameter_linknames",
                ]:
                    continue
                override_print.append("" + key2 + ": " + str(value2))

            parameters_string += " > override > " + str(override_print) + "\n"

    if "parameterbanks" in parameters:
        parameters_string += "banks:\n"
        for key, value in parameters["parameterbanks"].items():
            parameters_string += (
                "\t"
                + str(value["index"])
                + ((" (" + value["name"] + ")") if value["name"] != "" else "")
                + ": "
                + str(value["parameters"])
            )

    return "\nparameters:\n" + parameters_string


def get_dependency_cache_string_block(dependency_cache):
    if len(dependency_cache) > 0:
        return ""

    dependency_cache_string = ""
    for dependency in dependency_cache:
        dependency_cache_string += "\t" + str(dependency) + "\n"

    return (
        "\ndependency_cache:\n" + dependency_cache_string
        if dependency_cache_string != ""
        else ""
    )


def get_appversion_string_short(appversion):
    return f"appversion: {appversion['major']}.{appversion['minor']}.{appversion['revision']}-{appversion['architecture']}-{appversion['modernui']}"


def get_project_string_block(project):
    project_string = ""
    for key, value in project.items():
        if key != "contents":
            project_string = concat(project_string, key + ": " + get_property_string(value))
    if "contents" in project:
        contents_string = ""
        for key2, value2 in project["contents"].items():
            key3_string = ""
            for key3 in value2:
                key3_string += "\n\t\t\t" + key3
            if key3_string != "":
                contents_string += "\n\t\t" + key2 + ":" + key3_string
        if contents_string != "":
            project_string += "\n\tcontents:" + contents_string

    return "\nproject:\n\t" + project_string


def get_styles_string_block(styles, indent):
    return "\n" + ("\t") * indent + "styles: " + str(styles)


def get_object_parameter_string(parameter):
    parameter_string = ""
    for key, value in parameter.items():
        key_text = key[len("parameter_") :] if key.startswith("parameter_") else key
        parameter_string = concat(
            parameter_string, key_text + ": " + get_property_string(value)
        )

    return parameter_string



def concat(a, b):
    sep = " | "
    return sep.join(filter(None, [a, b]))


color_properties = [
    "slidercolor",
    "bgcolor",
    "bordercolor",
    "bordercolor2",
    "bgstepcolor",
    "tricolor",
    "tribordercolor",
    "panelcolor",
    "hltcolor",
    "needlecolor",
    "activeneedlecolor",
    "circlecolor",
    "activetricolor",
    "tricolor2",
    "activebgcolor",
    "bgrulercolor",
    "bgfillcolor",
    "blinkcolor",
    "bgoncolor",
    "stepcolor",
    "modulationcolor",
    "circleoncolor",
    "fgdialcolor",
    "activefgdialcolor",
    "dialcolor",
    "focusbordercolor",
    "locked_bgcolor",
    "editing_bgcolor",
    "bgstepcolor2",
    "bgunitcolor",
    "lcdbgcolor",
    "lcdcolor",
    "inactivelcdcolor",
    "linecolor",
    "activetricolor2",
    "activeslidercolor",
    "directioncolor",
    "textcolor",
    "activetextcolor",
    "textovercolor",
    "inactivetextoffcolor",
    "textoffcolor",
    "trioncolor",
    "arrowcolor",
    "textoncolor",
    "activetextoncolor",
    "hlttextcolor",
    "labeltextcolor",
    "inactivetextoncolor",
    "activebgoncolor",
]


def indent(text, amount, ch="\t"):
    padding = amount * ch
    return "".join(padding + line for line in text.splitlines(True))
