from freezing_utils import *


def print_frozen_device(data: bytes) -> str:
    """Parses a frozen device represented as bytes and returns a string representation of it."""
    footer_data_size = int.from_bytes(
        data[8:16], byteorder="big"
    )  # data size int is 64 bit
    footer_data = data[footer_data_size:]

    if footer_data[:4].decode("ascii") != "dlst":
        return "Error parsing footer data; footer data does not start with 'dlst'"
    footer_size = int.from_bytes(footer_data[4:8], byteorder="big")
    if footer_size != len(footer_data):
        return "Error parsing footer data; recorded size does not match actual size"

    frozen_string = "Device is frozen\n----- Contents -----\n"

    footer_entries = parse_footer(footer_data[8:])
    device_entries = get_device_entries(data, footer_entries)
    for entry in device_entries:
        if isinstance(entry["description"], str):
            frozen_string += entry["description"] + "\n"
    return frozen_string


def get_device_entries(
    data: bytes, footer_entries: list[footer_entry]
) -> list[device_entry_with_data]:
    """Converts footer entries to dict containing footer entry information and data."""
    entries: list[device_entry_with_data] = []

    for fields in footer_entries:
        if (
            "type" in fields
            and "fnam" in fields
            and "of32" in fields
            and "sz32" in fields
            and "mdat" in fields
        ):
            type_field = fields["type"]
            name_field = fields["fnam"]
            offset_field = fields["of32"]
            size_field = fields["sz32"]
            date_field = fields["mdat"]
            if not (
                isinstance(type_field, str)
                and isinstance(name_field, str)
                and isinstance(offset_field, int)
                and isinstance(size_field, int)
                and isinstance(date_field, datetime.datetime)
            ):
                raise Exception("Incorrect type for parsed footer fields")

            description = f'{name_field}: {size_field} bytes, modified at {date_field.strftime("%Y/%m/%d %T")} UTC'
            entry_data = data[offset_field : offset_field + size_field]
            entry: device_entry_with_data = {
                "file_name": name_field,
                "description": description,
                "type": type_field,
                "data": entry_data,
            }
            entries.append(entry)
    return entries
