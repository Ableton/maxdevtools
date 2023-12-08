import sys, gzip

def main(argv):
    inputfile = ''
    if (len(argv) != 1):
        print('Requires the file to convert as an argument')
        sys.exit(2)
    printAls(argv[0])

def printAls(path):
    if isGzipped(path):
        with gzip.open(path, 'rb') as fileObj:
            data = fileObj.read()
            print(data.decode("ascii"))
    else:
        with open(path, 'rb') as fileObj:
            data = fileObj.read()
            print(data.decode("ascii"))

def isGzipped(path):
    with open(path, 'rb') as fileObj:
        return fileObj.read(2) == b'\x1f\x8b'

if __name__ == "__main__":
   main(sys.argv[1:])
