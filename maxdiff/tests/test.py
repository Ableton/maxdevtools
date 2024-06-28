# Tests if the content of the test scripts is equal to the result of the conversion scripts.
# If not, displays the diff between the two.

import sys
import unittest
from io import StringIO
from unittest.mock import patch
import os.path
from test_parse import parse


class TestStringMethods(unittest.TestCase):
    def test_parse_device(self):
        self.maxDiff = None

        expected_path, test_path = get_test_path_files("EncryptedTest.amxd")

        with open(expected_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_path)
            self.assertEqual(expected, actual)

    def test_parse_encrypted_device(self):
        self.maxDiff = None

        expected_path, test_path = get_test_path_files("Test.amxd")

        with open(expected_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_path)
            self.assertEqual(expected, actual)

    def test_parse_frozen_device(self):
        self.maxDiff = None

        expected_path, test_path = get_test_path_files("FrozenTest.amxd")

        with open(expected_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_path)
            self.assertEqual(expected, actual)

    def test_parse_maxpat(self):
        self.maxDiff = None

        expected_path, test_path = get_test_path_files("Test.maxpat")

        with open(expected_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_path)

            self.assertEqual(expected, actual)

    def test_parse_als_zipped(self):
        self.maxDiff = None

        expected_path, test_path = get_test_path_files("/Test Project/Zipped.als")

        with open(expected_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_path)
            self.assertEqual(expected, actual)

    def test_parse_als_unzipped(self):
        self.maxDiff = None

        # result of an unzipped set should be same as a zipped set
        expected_path, test_path = get_test_path_files("/Test Project/Test.als")

        with open(expected_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_path)
            self.assertEqual(expected, actual)

    def test_parse_malformed_maxpat(self):
        self.maxDiff = None

        expected_path, test_path = get_test_path_files("MalFormedJsonTest.maxpat")

        with open(expected_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_path)
            self.assertEqual(expected, actual)

    def test_parse_maxpat_with_merge_conficts(self):
        self.maxDiff = None

        expected_path, test_path = get_test_path_files("ConflictMarkerTest.maxpat")

        with open(expected_path, mode="r") as expected_file:
            expected = expected_file.read()
            actual = parse(test_path)
            self.assertEqual(expected, actual)


def get_test_path_files(file_name):
    expected = get_test_path_file(f"test_baselines/{file_name}.txt")
    test = get_test_path_file(f"test_files/{file_name}")

    return (expected, test)


def get_test_path_file(file_name):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), file_name))


if __name__ == "__main__":
    unittest.main()
