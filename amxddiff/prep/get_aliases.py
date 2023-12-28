import sys
import json


def main(argv):
    inputfile = ""
    if len(argv) != 1:
        print("Requires the path to Max.app")
        sys.exit(2)
    all_aliases = {}
    for source in ["audio", "max", "jitter"]:
        aliases = get_aliases(f"{argv[0]}/Contents/Resources/C74/init/{source}-objectmappings.txt")

        for key, value in aliases.items():
            all_aliases[key] = value

    print(json.dumps(all_aliases, indent=4))


def get_aliases(path):
    print("Parsing ", path)
    with open(path, "r", encoding="utf-8") as file_obj:
        lines = file_obj.readlines()
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
