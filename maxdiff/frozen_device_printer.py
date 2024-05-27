import datetime


def print_frozen_device(data):
    """Parses a frozen device and returns a textual representation of it."""
    dependency_data_size = int.from_bytes(
        data[8:16], byteorder="big"
    )  # data size int is 64 bit
    footer_data = data[dependency_data_size:]

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


def parse_footer(data):
    """Parses the footer data of a frozen device and returns an array of
    string representations of the frozen dependencies."""
    dependencies = []
    while data[:4].decode("ascii") == "dire":
        size = int.from_bytes(data[4:8], byteorder="big")
        fields = get_fields(data[8 : 8 + size])
        if "fnam" in fields and "sz32" in fields and "mdat" in fields:
            dependencies.append(
                f'{fields["fnam"]}: {fields["sz32"]} bytes, modified at {fields["mdat"].strftime("%Y/%m/%d %T")}'
            )
        data = data[size:]
    return dependencies


def get_fields(data):
    """Parses the data for a frozen dependency and returns a dict of its fields and their contents."""
    fields = {}
    while len(data) > 12:
        field_type = data[:4].decode("ascii")
        field_size = int.from_bytes(data[4:8], byteorder="big")
        field_data = data[8:field_size]
        fields[field_type] = parse_field_data(field_type, field_data)

        data = data[field_size:]
    return fields


def parse_field_data(field_type, data):
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
    return


def remove_trailing_zeros(data: bytes) -> bytes:
    """Remove trailing zeros from a zero-padded byte representation of a string"""
    first_trailing_zero = -1
    for i in range(len(data) - 1, -1, -1):
        if data[i] != 0:
            first_trailing_zero = i + 1
            break

    if first_trailing_zero != -1:
        return data[:first_trailing_zero]
    return data


def get_hfs_date(data):
    """Converts a byte sequence that represents a HFS+ date to a Python datetime object"""
    seconds_offset_from_unix = 2082844800  # Mac HFS+ is time since 1 Jan 1904 while Unix time is since 1 Jan 1970
    seconds_in_hfs_plus = int.from_bytes(data, byteorder="big")
    return datetime.datetime.fromtimestamp(
        seconds_in_hfs_plus - seconds_offset_from_unix
    )
