# Tests if the content of Test.txt is equal to the result of amxdTextConv.
# If not, displays the diff between the two.

import sys
import unittest
import difflib

import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import amxdTextconv
import maxpatTextconv


class TestStringMethods(unittest.TestCase):
    def test_parse_device(self):
        self.maxDiff = None

        expectedFilePath = getTestPathFile("EncryptedTest.amxd.txt")
        testFilePath = getTestPathFile("EncryptedTest.amxd")

        with open(expectedFilePath, mode="r") as expectedFile:
            expected = expectedFile.read()
            actual = parse(testFilePath)
            self.assertEqual(expected, actual)

    def test_parse_encrypted_device(self):
        self.maxDiff = None

        expectedFilePath = getTestPathFile("Test.amxd.txt")
        testFilePath = getTestPathFile("Test.amxd")

        with open(expectedFilePath, mode="r") as expectedFile:
            expected = expectedFile.read()
            actual = parse(testFilePath)
            self.assertEqual(expected, actual)

    def test_parse_maxpat(self):
        self.maxDiff = None

        expectedFilePath = getTestPathFile("Test.maxpat.txt")
        testFilePath = getTestPathFile("Test.maxpat")

        with open(expectedFilePath, mode="r") as expectedFile:
            expected = expectedFile.read()
            actual = parse(testFilePath)
            self.assertEqual(expected, actual)


def parse(path):
    result = (
        maxpatTextconv.parse(path)
        if path.endswith(".maxpat")
        else amxdTextconv.parse(path)
    )
    return result


def getTestPathFile(fileName):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), fileName))


if __name__ == "__main__":
    unittest.main()
