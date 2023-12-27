import sys, gzip


def main(argv):
    if len(argv) != 1:
        print("Requires the file to convert as an argument")
        sys.exit(2)
    result = parse(argv[0])
    print(result)


def parse(path):
    if is_gzipped(path):
        with gzip.open(path, "rb") as file_obj:
            data = file_obj.read()
            return data.decode("ascii")
    else:
        with open(path, "rb") as file_obj:
            data = file_obj.read()
            return data.decode("ascii")


def is_gzipped(path):
    with open(path, "rb") as file_obj:
        return file_obj.read(2) == b"\x1f\x8b"


if __name__ == "__main__":
    main(sys.argv[1:])
