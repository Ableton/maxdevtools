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
