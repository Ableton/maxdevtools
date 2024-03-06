"""
Module that shares a function to gracefully handle printing unicode characters 
if the user has the PYTHONIOENCODING environment vairable set to 'ascii'. 
In that case, replace any characters that can't be encoded with ?.
"""


def print_unicode_string(s):
    try:
        print(s)
    except UnicodeEncodeError:
        string_bytes = s.encode("ascii", "backslashreplace")
        print(string_bytes.decode("ascii"))
