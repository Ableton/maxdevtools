import json
import datetime
from typing import Optional

footer_entry = dict[str, str | int | datetime.datetime | None]
device_entry_with_data = dict[str, str | bytes]


def parse_footer(data: bytes) -> list[footer_entry]:
    """Parses the byte data of a frozen device footer and returns a list of frozen dependencies."""
    footer_entries: list[footer_entry] = []
    while data[:4].decode("ascii") == "dire":
        size = int.from_bytes(data[4:8], byteorder="big")
        fields = get_fields(data[8 : 8 + size])
        footer_entries.append(fields)
        data = data[size:]
    return footer_entries


def get_fields(data: bytes) -> footer_entry:
    """Parses the data for a frozen dependency and returns a dict of its fields and their contents."""
    fields = {}
    while len(data) >= 12:
        field_type = data[:4].decode("ascii")
        field_size = int.from_bytes(data[4:8], byteorder="big")
        field_data = data[8:field_size]
        fields[field_type] = parse_field_data(field_type, field_data)

        data = data[field_size:]
    return fields


def parse_field_data(
    field_type: str, data: bytes
) -> Optional[str | int | datetime.datetime]:
    """Parses the data of a field. Depending on the field type, returns its data as the correct type"""
    match field_type:
        case "type":
            return remove_trailing_zeros(data).decode("ascii")
        case "fnam":
            return remove_trailing_zeros(data).decode("ascii")
        case "sz32":
            return int.from_bytes(data, byteorder="big")
        case "of32":
            return int.from_bytes(data, byteorder="big")
        case "vers":
            return int.from_bytes(data, byteorder="big")
        case "flag":
            return int.from_bytes(data, byteorder="big")
        case "mdat":
            return get_hfs_date(data)
    return None


def remove_trailing_zeros(data: bytes) -> bytes:
    """Remove trailing zeros from a zero-padded byte representation of a string"""
    return data.rstrip(b"\x00")


def get_hfs_date(data: bytes) -> datetime.datetime:
    """Converts a byte sequence that represents a HFS+ date to a Python datetime object"""
    seconds_offset_from_unix = 2082844800  # Mac HFS+ is time since 1 Jan 1904 while Unix time is since 1 Jan 1970
    seconds_in_hfs_plus = int.from_bytes(data, byteorder="big")
    return datetime.datetime.fromtimestamp(
        seconds_in_hfs_plus - seconds_offset_from_unix, datetime.UTC
    )


def get_patcher_dict(entry: device_entry_with_data):
    """Returns the dict that represents the given patcher data.
    Prints errors if parsing fails"""

    if not "data" in entry:
        return {}

    patch_data = entry["data"]
    if not isinstance(patch_data, bytes):
        return {}

    if not "file_name" in entry:
        return {}

    name = entry["file_name"]
    if not isinstance(name, str):
        return {}

    device_data_text = ""
    try:
        device_data_text = patch_data.decode("utf-8")

        # Past Max versions could write patcher data with a trailing 0
        # or with trailing garbage.
        device_data_text = strip_trailing_nonjson(device_data_text)
    except Exception as e:
        print(f"Error getting patch data as text for entry {name}: {e}")
        return {}

    try:
        patcher_dict = json.loads(device_data_text)
    except ValueError as e:
        print(f"Error parsing device patch data as json for entry {name}: {e}")
        return {}

    try:
        patcher = patcher_dict["patcher"]
        return patcher
    except:
        print(f"Content of entry {name} does not seem to be a patcher")
        return {}


def strip_trailing_nonjson(device_data_text: str) -> str:
    """
    This function returns (possibly trimmed) JSON text to pass to json.loads().
    """
    decoder = json.JSONDecoder()
    try:
        _, end = decoder.raw_decode(device_data_text)
        return device_data_text[:end].rstrip()
    except json.JSONDecodeError:
        pass

    # find all candidate closing positions for objects/arrays
    closers = [i for i, ch in enumerate(device_data_text) if ch in ("}", "]")]
    # try from last to first — prefer the longest valid prefix
    for pos in reversed(closers):
        candidate = device_data_text[: pos + 1]
        try:
            json.loads(candidate)
            return candidate
        except Exception:
            continue

    # nothing worked; return original so caller can log/handle the parse error
    return device_data_text
