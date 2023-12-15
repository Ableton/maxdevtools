import sys, json


def main(argv):
    inputfile = ""
    if len(argv) != 1:
        print("Requires the path to Max.app")
        sys.exit(2)
    allAliases = {}
    for source in ["audio", "max", "jitter"]:
        aliases = getAliases(
            argv[0] + "/Contents/Resources/C74/init/" + source + "-objectmappings.txt"
        )
        for key, value in aliases.items():
            allAliases[key] = value

    print(json.dumps(allAliases))


def getAliases(path):
    print("Parsing ", path)
    with open(path, "r", encoding="utf-8") as fileObj:
        lines = fileObj.readlines()
        aliases = {}
        for line in lines:
            if line == "\n" or line == "":
                continue
            tokens = line.split()
            alias = tokens[2]
            reference = tokens[len(tokens) - 1][0:-1]
            aliases[alias] = reference
        return aliases
    return {}


if __name__ == "__main__":
    main(sys.argv[1:])
