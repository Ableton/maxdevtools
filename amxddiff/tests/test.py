# Tests if the content of Test.txt is equal to the result of amxdTextConv.
# If not, displays the diff between the two.

import sys
import unittest
import difflib

import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import amxdTextconv
import maxpatTextconv
import alsTextconv


class TestStringMethods(unittest.TestCase):
    def test_parse_device(self):
        self.maxDiff = None

        expectedFilePath = getTestPathFile("testBaselines/EncryptedTest.amxd.txt")
        testFilePath = getTestPathFile("testFiles/EncryptedTest.amxd")

        with open(expectedFilePath, mode="r") as expectedFile:
            expected = expectedFile.read()
            actual = parse(testFilePath)
            self.assertEqual(expected, actual)

    def test_parse_encrypted_device(self):
        self.maxDiff = None

        expectedFilePath = getTestPathFile("testBaselines/Test.amxd.txt")
        testFilePath = getTestPathFile("testFiles/Test.amxd")

        with open(expectedFilePath, mode="r") as expectedFile:
            expected = expectedFile.read()
            actual = parse(testFilePath)
            self.assertEqual(expected, actual)

    def test_parse_maxpat(self):
        self.maxDiff = None

        expectedFilePath = getTestPathFile("testBaselines/Test.maxpat.txt")
        testFilePath = getTestPathFile("testFiles/Test.maxpat")

        with open(expectedFilePath, mode="r") as expectedFile:
            expected = expectedFile.read()
            actual = parse(testFilePath)
            self.assertEqual(expected, actual)

    def test_parse_als_zipped(self):
        self.maxDiff = None

        expectedFilePath = getTestPathFile("testBaselines/Test.als.txt")
        testFilePath = getTestPathFile("testFiles/Test Project/Test.als")

        with open(expectedFilePath, mode="r") as expectedFile:
            expected = expectedFile.read()
            actual = parse(testFilePath)
            self.assertEqual(expected, actual)

    def test_parse_als_unzipped(self):
        self.maxDiff = None

        # result of an unzipped set should be same as a zipped set
        expectedFilePath = getTestPathFile("testBaselines/Test.als.txt")
        testFilePath = getTestPathFile("testFiles/Test Project/Test-NoZip.als")

        with open(expectedFilePath, mode="r") as expectedFile:
            expected = expectedFile.read()
            actual = parse(testFilePath)
            self.assertEqual(expected, actual)


def parse(path):
    result = ""
    if path.endswith(".amxd"):
        result = amxdTextconv.parse(path)
    if path.endswith(".maxpat"):
        result = maxpatTextconv.parse(path)
    if path.endswith(".als"):
        result = alsTextconv.parse(path)
    return result


def getTestPathFile(fileName):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), fileName))


if __name__ == "__main__":
    unittest.main()
