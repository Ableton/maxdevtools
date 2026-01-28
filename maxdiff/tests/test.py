# Tests if the contents of the stored textual representations (the baselines)
# are still equal to the results of the maxdiff conversion script.
# If not, displays the diff between the two.

import unittest
from unittest.mock import patch
import os.path
from test_parse import parse


class TestStringMethods(unittest.TestCase):
    def test_all_parsing(self):
        self.maxDiff = None

        files = [
            "Test.amxd",
            "EncryptedTest.amxd",
            "FrozenTest.amxd",
            "Test.maxpat",
            "PatcherWithLocalStyles.maxpat",
            "/Test Project/Zipped.als",
            "/Test Project/Test.als",
            "MalFormedJsonTest.maxpat",
            "ConflictMarkerTest.maxpat",
            "WithGarbage.amxd",
        ]

        for file_name in files:
            with self.subTest(file=file_name):
                self.assertDiffsEqual(file_name)

    def assertDiffsEqual(self, file_name):
        test_path = get_test_path_file(f"test_files/{file_name}")
        expected_path = get_test_path_file(f"test_baselines/{file_name}.txt")

        with open(expected_path, mode="r") as expected_file:
            expected = expected_file.read()
        actual = parse(test_path)
        self.assertEqual(expected, actual)


def get_test_path_file(file_name):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), file_name))


if __name__ == "__main__":
    unittest.main()
