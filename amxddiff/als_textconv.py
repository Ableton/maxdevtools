import sys, gzip, argparse


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


def main():
    parser = argparse.ArgumentParser(
        description="Convert ALS file to a textual representation."
    )
    parser.add_argument("file", type=str, help="Path to the file to convert")
    args = parser.parse_args()

    try:
        result = parse(args.file)
        print(result)
    except RuntimeError:
        sys.exit(2)


if __name__ == "__main__":
    main()
