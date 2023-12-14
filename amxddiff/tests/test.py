# Tests if the content of Test.txt is equal to the result of amxdTextConv.
# If not, displays the diff between the two.

import sys
from io import StringIO
import difflib

import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

import amxdTextconv

def main():
    expectedFile = os.path.abspath(os.path.join(os.path.dirname(__file__), "Test.txt"))
    testFile = os.path.abspath(os.path.join(os.path.dirname(__file__), "Test.amxd"))
    encryptedExpectedFile = os.path.abspath(os.path.join(os.path.dirname(__file__), "EncryptedTest.txt"))
    encryptedTestFile = os.path.abspath(os.path.join(os.path.dirname(__file__), "EncryptedTest.amxd"))

    with open(expectedFile, mode='r') as toCompare:
        expected = toCompare.read()
        actual = amxdTextconv.parseAmxd(testFile)
        printResult(expected, actual, "Parse device")

    with open(encryptedExpectedFile, mode='r') as toCompare:
        expected = toCompare.read()
        actual = amxdTextconv.parseAmxd(encryptedTestFile)
        printResult(expected, actual, "Parse encrypted device")

def printResult(expected, actual, testName):
    if actual == expected:
        print('\033[1m' + '\033[32m' + "Test successful: " + testName + '\033[0m')
    else:
        print('\033[1m' + '\033[31m' + "Test failed: " + testName + '\033[0m')
        print("Expected: " + str(len(expected)) + " characters, got " + str(len(actual)))
        print("--- How the actual result differs from the expected result: ---")
        print(diffString(expected, actual))
    
def diffString(a, b):
    output = []
    matcher = difflib.SequenceMatcher(None, a, b)
    for opcode, a0, a1, b0, b1 in matcher.get_opcodes():
        if opcode == "equal":
            output.append(a[a0:a1])
        elif opcode == "insert":
            inserted = b[b0:b1] if b[b0:b1] != "\n" else "-- new line --\n"
            output.append('\033[32m' + inserted + '\033[0m')
        elif opcode == "delete":
            deleted = a[a0:a1] if a[a0:a1] != "\n" else "-- new line --\n"
            output.append('\033[31m' + deleted + '\033[0m')
        elif opcode == "replace":
            inserted = b[b0:b1] if b[b0:b1] != "\n" else "-- new line --\n"
            deleted = a[a0:a1] if a[a0:a1] != "\n" else "-- new line --\n"
            output.append('\033[32m' + inserted + '\033[0m')
            output.append('\033[31m' + deleted + '\033[0m')
    return "".join(output)    

if __name__ == "__main__":
    main()