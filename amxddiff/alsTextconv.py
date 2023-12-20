import sys, gzip


def main(argv):
    if len(argv) != 1:
        print("Requires the file to convert as an argument")
        sys.exit(2)
    result = parse(argv[0])
    print(result)


def parse(path):
    if isGzipped(path):
        with gzip.open(path, "rb") as fileObj:
            data = fileObj.read()
            return data.decode("ascii")
    else:
        with open(path, "rb") as fileObj:
            data = fileObj.read()
            return data.decode("ascii")


def isGzipped(path):
    with open(path, "rb") as fileObj:
        return fileObj.read(2) == b"\x1f\x8b"


if __name__ == "__main__":
    main(sys.argv[1:])
