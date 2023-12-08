import sys, json
import collections
from patchPrinter import printPatcher

def main(argv):
    if (len(argv) != 1):
        print('Requires the file to convert as an argument')
        sys.exit(2)
    parseAmxd(argv[0])

def parseAmxd(path):
    with open(path, 'rb') as fileObj:
        encrypted = False
        while True:
            chunk = fileObj.read(4)
            if len(chunk) < 4:
                break

            field = chunk.decode("ascii")
            datasize = int.from_bytes(fileObj.read(4), byteorder='little')
            data = fileObj.read(datasize)

            encrypted = parseField(field, datasize, data, encrypted)

def parseField(field, datasize, data, encrypted) :
    if field == 'ampf':
        if datasize != 4:
            print('Incorrect device type argument')
            sys.exit(2)
        devicetype = data.decode("ascii")
        if devicetype == "aaaa":
            print("Audio Effect Device")
        elif devicetype == "mmmm":
            print("MIDI Effect Device")
        elif devicetype == "iiii":
            print("Instrument Device")
        else:
            print("Unknown device type")
        print("-------------------")
        return encrypted
    elif field == 'ptch':
        if encrypted:
            print('<Patch is encrypted>')
            return encrypted
        if data[:4].decode("ascii") ==  "mx@c":
            print ("Device is frozen")
        else:
            if (data[datasize-1] == 0):
                # json.loads doesn't like if there is a value of 0
                # at the end of the string which Max appears to add
                patcherDict = json.loads(data[:datasize-1].decode("utf-8"))
            else:
                # but we also want to support if the JSON is written by JS.
                patcherDict = json.loads(data.decode("utf-8"))
            printPatcher(patcherDict)
        return encrypted
    elif field == 'meta':
        #unused
        return encrypted
    elif field == 'ciph':
        print('----- Cipher -----')
        print("..." + data[datasize-8:datasize].hex()) # print last part of cipher to show if there is a difference
        return True
    else:
        print('Unknown field', field)
        sys.exit(2)


if __name__ == "__main__":
   main(sys.argv[1:])
