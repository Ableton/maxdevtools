import sys, json
from patch_printer import print_patcher


def main(argv):
    if len(argv) != 1:
        print("Requires the file to convert as an argument")
        sys.exit(2)
    print(parse(argv[0]))


def parse(path):
    with open(path, "r", encoding="utf-8") as file_obj:
        patcher_dict = json.load(file_obj)
        return print_patcher(patcher_dict)


if __name__ == "__main__":
    main(sys.argv[1:])
