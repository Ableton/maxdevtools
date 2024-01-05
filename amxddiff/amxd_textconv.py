"""Module to convert an AMXD file to a textual representation that can then be diffed."""
import sys
import json
import argparse
from patch_printer import print_patcher


def parse(path: str) -> str:
    """Parse a file and returns a textual representation of it."""
    result = ""
    with open(path, "rb") as file_obj:
        encrypted = False
        while True:
            chunk = file_obj.read(4)
            if len(chunk) < 4:
                break

            field = chunk.decode("ascii")
            datasize = int.from_bytes(file_obj.read(4), byteorder="little")
            data = file_obj.read(datasize)

            if field == "ciph":
                encrypted = True

            if field == "ptch" and encrypted:
                result += "<Patch is encrypted>\n"
            else:
                result += parse_field(field, datasize, data)
    return result


def parse_field(field: str, datasize: int, data: bytes) -> str:
    """Select the correct handler for the field and device type."""
    device_types = {
        "aaaa": "Audio Effect Device",
        "mmmm": "MIDI Effect Device",
        "iiii": "Instrument Device",
        "nagg": "MIDI Tool Generator",
        "natt": "MIDI Tool Transformation",
    }

    field_handlers = {
        "ampf": handle_ampf,
        "meta": handle_meta,
        "ciph": handle_ciph,
        "ptch": handle_ptch,
    }

    if field in field_handlers:
        return field_handlers[field](datasize, data, device_types)
    else:
        raise RuntimeError(f"Unknown field {field}")


def handle_ampf(datasize: int, data: bytes, device_types: dict) -> str:
    """Handle the ampf field."""
    if datasize != 4:
        raise RuntimeError("Incorrect device type argument")
    devicetype = data.decode("ascii")
    return f"{device_types.get(devicetype, f'Unknown device type {devicetype}')}\n-------------------\n"


def handle_meta(datasize: int, data: bytes, device_types: dict):
    """Handle the meta field."""
    return ""


def handle_ciph(datasize: int, data: bytes, device_types: dict) -> str:
    """Handle the ciph field. This is used when a device is encrypted."""
    return f"----- Cipher -----\n...{data[datasize-8:datasize].hex()}\n"


def handle_ptch(datasize: int, data: bytes, device_types: dict) -> dict | str:
    """Handle the ptch field."""
    if data[:4].decode("ascii") == "mx@c":
        return "Device is frozen"
    else:
        if data[datasize - 1] == 0:
            patcher_dict = json.loads(data[: datasize - 1].decode("utf-8"))
        else:
            patcher_dict = json.loads(data.decode("utf-8"))
        return print_patcher(patcher_dict)


def main():
    """Entry point of the program."""
    parser = argparse.ArgumentParser(
        description="Convert AMXD file to a textual representation."
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
