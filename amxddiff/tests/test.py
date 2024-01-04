# Tests if the content of the test scripts is equal to the result of the conversion scripts.
# If not, displays the diff between the two.

import sys
import unittest
from io import StringIO
from unittest.mock import patch
import difflib

import os.path

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

import amxd_textconv
import maxpat_textconv
import als_textconv


class TestStringMethods(unittest.TestCase):
    def test_parse_device(self):
        self.maxDiff = None

        expected_file_path = get_test_path_file("test_baselines/EncryptedTest.amxd.txt")
        test_file_path = get_test_path_file("test_files/EncryptedTest.amxd")

        with open(expected_file_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_file_path)
            self.assertEqual(expected, actual)

    def test_parse_encrypted_device(self):
        self.maxDiff = None

        expected_file_path = get_test_path_file("test_baselines/Test.amxd.txt")
        test_file_path = get_test_path_file("test_files/Test.amxd")

        with open(expected_file_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_file_path)
            self.assertEqual(expected, actual)

    def test_parse_maxpat(self):
        self.maxDiff = None

        expected_file_path = get_test_path_file("test_baselines/Test.maxpat.txt")
        test_file_path = get_test_path_file("test_files/Test.maxpat")

        with open(expected_file_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_file_path)

            # print ("expected: " + expected)
            # print ("actual: " + actual)

            self.assertEqual(expected, actual)

    def test_parse_als_zipped(self):
        self.maxDiff = None

        expected_file_path = get_test_path_file("test_baselines/Test.als.txt")
        test_file_path = get_test_path_file("test_files/Test Project/Test.als")

        with open(expected_file_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_file_path)
            self.assertEqual(expected, actual)

    def test_parse_als_unzipped(self):
        self.maxDiff = None

        # result of an unzipped set should be same as a zipped set
        expected_file_path = get_test_path_file("test_baselines/Test.als.txt")
        test_file_path = get_test_path_file("test_files/Test Project/Test-NoZip.als")

        with open(expected_file_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_file_path)
            self.assertEqual(expected, actual)


def parse(path):
    mains = {
        ".amxd": amxd_textconv.main,
        ".maxpat": maxpat_textconv.main,
        ".als": als_textconv.main,
    }

    file_extension = os.path.splitext(path)[1]
    if file_extension in mains:
        # route std output to a cystom StringIO
        old_stdout = sys.stdout
        sys.stdout = actualStringIo = StringIO()

        # set the main arguments
        old_sys_argv = sys.argv
        sys.argv = [old_sys_argv[0]] + [path]

        # call the main function of the appropriate script
        try:
            patch("sys.argv", ["prog", path])
            mains[file_extension]()
        finally:
            sys.argv = old_sys_argv
            sys.stdout = old_stdout
        return actualStringIo.getvalue()[:-1]
    return ""


def get_test_path_file(file_name):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), file_name))


if __name__ == "__main__":
    unittest.main()
