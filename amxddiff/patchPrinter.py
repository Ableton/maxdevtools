from knownObjects import knownObjects
from defaultPatcher import defaultPatcher
from objectAliases import objectAliases


def printPatcher(patcherDict, summarize=True):
    """
    Prints a summary of a patcher dict.
    Note that the script should only format properties it knows about or is actively set to skip.
    Unknown or unexpected data should always be printed as raw json, so that the summary never discards valuable information.
    """
    if summarize:
        knownObjectsMap = {}
        for boxObj in knownObjects["boxes"]:
            box = boxObj["box"]
            name = getBoxText(box)
            knownObjectsMap[name] = box

        return printPatcherSummaryRecursive(patcherDict, knownObjectsMap)
    else:
        import json

        return json.dumps(patcherDict, indent=4, sort_keys=True)


def printPatcherSummaryRecursive(patcherDict, knownObjectsMap, indent=0):
    if (
        "patcher" not in patcherDict
        or "boxes" not in patcherDict["patcher"]
        or "lines" not in patcherDict["patcher"]
    ):
        return ""

    summaryString = ""

    patcher = patcherDict["patcher"]

    #### patcher ####

    skipPatcherProperties = [
        "boxes",  # iterated over later
        "lines",  # iterated over later
        "parameters",  # treated separately
        "dependency_cache",  # treated separately
        "project",  # treated separately
        "styles",  # treated separately
    ]

    properties = getPropertiesToPrint(patcher, defaultPatcher, skipPatcherProperties)

    displayText = ""
    for key, value in properties.items():
        if key == "appversion":
            displayText += getAppversionStringShort(value)
            continue

        displayText = concat(displayText, key + ": " + getPropertyString(value))

    if "parameters" in patcher:
        displayText += getParametersStringBlock(patcher["parameters"])

    if "dependency_cache" in patcher:
        displayText += getDependencyCacheStringBlock(patcher["dependency_cache"])

    if "project" in patcher:
        displayText += getProjectStringBlock(patcher["project"])

    if "styles" in patcher:
        displayText += getStylesStringBlock(patcher["styles"], indent)

    if displayText != "":
        summaryString += ("\t") * indent + displayText + "\n"

    #### objects ####

    if not patcher["boxes"]:
        return

    summaryString += ("\t") * indent + "----------- objects -----------" + "\n"

    # every entry of "boxes" has a single item "box"
    boxes = list(map(lambda val: val["box"], patcher["boxes"]))

    # we sort the boxes to make the same patches look equal
    boxes.sort(key=getBoxText)

    skipBoxProperties = [
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

    idsToNames = {}
    for box in boxes:
        boxText = getBoxText(box)

        idsToNames[box["id"]] = boxText

        displayText = ""
        objectName = boxText.split()[0]

        if objectName not in knownObjectsMap and objectName in objectAliases:
            objectName = objectAliases[objectName]

        defaultBox = {}
        if objectName in knownObjectsMap:
            defaultBox = knownObjectsMap[objectName]

        properties = getPropertiesToPrint(box, defaultBox, skipBoxProperties)

        for key, value in properties.items():
            displayText = concat(displayText, key + ": " + getPropertyString(value))

        summaryString += ("\t") * indent + "[" + boxText + "] " + displayText + "\n"

        if "patcher" in box:
            summaryString += printPatcherSummaryRecursive(
                box, knownObjectsMap, indent + 1
            )

    #### patch cords ####

    if len(patcher["lines"]) == 0:
        return summaryString

    summaryString += ("\t") * indent + "----------- patch cords -----------" + "\n"

    lines = []
    for val in patcherDict["patcher"]["lines"]:
        lines.append(val["patchline"])

    def lineSort(line):
        return idsToNames[line["source"][0]]

    lines.sort(key=lineSort)

    # We don't try to vertically align the sources and destinations of the lines,
    # even though that might make this more readable; a change in the maximum
    # source object length would affect all other printed lines

    for line in lines:
        fromName = "[" + idsToNames[line["source"][0]] + "]"
        fromOutlet = "(" + str(line["source"][1]) + ")"
        toName = "[" + idsToNames[line["destination"][0]] + "]"
        toInlet = "(" + str(line["destination"][1]) + ")"

        displayText = fromName + " " + fromOutlet + " => " + toInlet + " " + toName
        summaryString += ("\t") * indent + displayText + "\n"

    return summaryString


def getBoxText(box):
    objecttype = box["maxclass"]
    boxtext = objecttype
    if objecttype == "newobj":
        boxtext = box["text"]
    elif "text" in box:
        boxtext = objecttype + " " + box["text"]

    if objecttype == "bpatcher" and "name" in box:
        boxtext = boxtext + " " + box["name"]

    return boxtext


def getPropertiesToPrint(boxOrPatcher, default, skipProperties):
    properties = {}
    for key, value in boxOrPatcher.items():
        if key in skipProperties:
            continue

        if key in default and default[key] == value:
            continue

        if value == "":
            # TODO: are we sure there are no properties that have default values of some string but can be set to an empty string?
            continue

        if key == "saved_attribute_attributes":
            # We take the attributes out or saved_attribute_attributes and present them as properties
            attributes = getSavedAttributeAttributes(value)
            attributesToPrint = getPropertiesToPrint(attributes, default, skipProperties)
            for newKey, newValue in attributesToPrint.items():
                properties[
                    newKey
                ] = newValue  # this may overwrite existing value-based colors. This is ok, we want dynamic color values instead.
            continue

        if key == "saved_object_attributes":
            # We take the attributes out or saved_object_attributes and present them as properties
            attributes = getSavedObjectAttributes(value)
            attributesToPrint = getPropertiesToPrint(attributes, default, skipProperties)
            for newKey, newValue in attributesToPrint.items():
                properties[newKey] = newValue
            continue

        if key not in properties:
            # Don't overwrite existing dynamic colors
            properties[key] = value

    return properties


def getPropertyString(value):
    if isinstance(value, list):
        s = ""
        for item in value:
            if s != "":
                s += ", "

            if isinstance(item, float):
                if item.is_integer():
                    s += "{:.0f}".format(item)
                else:
                    s += "{:.2f}".format(item)
            else:
                s += str(item)
        return "[" + s + "]"

    return str(value)


def getSavedAttributeAttributes(value):
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


def getSavedObjectAttributes(value):
    result = {}
    for attrkey, attrvalue in value.items():
        if attrvalue == "":
            continue

        result[attrkey] = attrvalue
    return result


def getParametersStringBlock(parameters):
    s = ""
    for key, value in parameters.items():
        if key in ["parameter_overrides", "parameterbanks"]:
            continue

        if (
            "parameter_overrides" in parameters
            and key in parameters["parameter_overrides"]
        ):
            s += "\t" + key + " " + str(value)

            override = parameters["parameter_overrides"][key]
            overridePrint = []
            overridePrint.append(
                override["parameter_longname"]
                if ("parameter_longname" in override)
                else "-"
            )
            overridePrint.append(
                override["parameter_shortname"]
                if ("parameter_shortname" in override)
                else "-"
            )
            overridePrint.append(
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
                overridePrint.append("" + key2 + ": " + str(value2))

            s += " > override > " + str(overridePrint) + "\n"

    if "parameterbanks" in parameters:
        s += "banks:\n"
        for key, value in parameters["parameterbanks"].items():
            s += (
                "\t"
                + str(value["index"])
                + ((" (" + value["name"] + ")") if value["name"] != "" else "")
                + ": "
                + str(value["parameters"])
            )

    return "\nparameters:\n" + s


def getDependencyCacheStringBlock(dependencyCache):
    if len(dependencyCache) > 0:
        return ""

    s = ""
    for dependency in dependencyCache:
        s += "\t" + str(dependency) + "\n"

    return "\ndependency_cache:\n" + s if s != "" else ""


def getAppversionStringShort(appversion):
    return f"appversion: {appversion['major']}.{appversion['minor']}.{appversion['revision']}-{appversion['architecture']}-{appversion['modernui']}"


def getProjectStringBlock(project):
    projectString = ""
    for key, value in project.items():
        if key != "contents":
            projectString = concat(projectString, key + ": " + getPropertyString(value))
    if "contents" in project:
        contentsString = ""
        for key2, value2 in project["contents"].items():
            key3String = ""
            for key3 in value2:
                key3String += "\n\t\t\t" + key3
            if key3String != "":
                contentsString += "\n\t\t" + key2 + ":" + key3String
        if contentsString != "":
            projectString += "\n\tcontents:" + contentsString

    return "\nproject:\n\t" + projectString


def getStylesStringBlock(styles, indent):
    return "\n" + ("\t") * indent + "styles: " + str(styles)


def getObjectParameterString(parameter):
    parameterString = ""
    for key, value in parameter.items():
        keyText = key[len("parameter_") :] if key.startswith("parameter_") else key
        parameterString = concat(
            parameterString, keyText + ": " + getPropertyString(value)
        )

    return parameterString


def concat(a, b):
    sep = " | "
    return sep.join(filter(None, [a, b]))


colorProperties = [
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
