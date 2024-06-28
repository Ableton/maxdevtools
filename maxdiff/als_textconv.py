"""Module to convert an ALS file to a textual representation that can then be diffed."""

import sys
import gzip
import argparse


def parse(path: str) -> str:
    """Parse a file and returns a textual representation of it."""
    if is_gzipped(path):
        with gzip.open(path, "rb") as file_obj:
            data = file_obj.read()
            return data.decode("ascii")
    else:
        with open(path, "rb") as file_obj:
            data = file_obj.read()
            return data.decode("ascii")


def is_gzipped(path: str) -> bool:
    """Check if a file is gzipped or not."""
    with open(path, "rb") as file_obj:
        return file_obj.read(2) == b"\x1f\x8b"


def main():
    """Entry point of the program."""
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
