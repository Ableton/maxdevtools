import sys, json
import collections
from patchPrinter import printPatcher

def main(argv):
    if (len(argv) != 1):
        print('Requires the file to convert as an argument')
        sys.exit(2)
    parsePatchFile(argv[0])

def parsePatchFile(path):
    with open(path, "r", encoding="utf-8") as fileObj:
        patcherDict = json.load(fileObj)
        printPatcher(patcherDict)

if __name__ == "__main__":
   main(sys.argv[1:])
