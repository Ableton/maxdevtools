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
    dependencies = parse_footer(footer_data[8:])
    for dependency in dependencies:
        frozen_string += dependency + "\n"
    return frozen_string


def parse_footer(footer_data: bytes) -> list[str]:
    """Parses the footer byte data of a frozen device and returns an array of
    string representations of the frozen dependencies."""
    dependencies: list[str] = []
    while footer_data[:4].decode("ascii") == "dire":
        size = int.from_bytes(footer_data[4:8], byteorder="big")
        fields = get_fields(footer_data[8 : 8 + size])
        if "fnam" in fields and "sz32" in fields and "mdat" in fields:
            name_field = fields["fnam"]
            size_field = fields["sz32"]
            date_field = fields["mdat"]
            if not (
                isinstance(name_field, str)
                and isinstance(size_field, int)
                and isinstance(date_field, datetime.datetime)
            ):
                raise Exception("Incorrect type for parsed footer fields")
            dependencies.append(
                f'{fields["fnam"]}: {fields["sz32"]} bytes, modified at {date_field.strftime("%Y/%m/%d %T")} UTC'
            )
        footer_data = footer_data[size:]
    return dependencies
