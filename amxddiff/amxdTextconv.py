import sys, json
from patchPrinter import printPatcher


def main(argv):
    if len(argv) != 1:
        print("Requires the file to convert as an argument")
        sys.exit(2)
    print(parseAmxd(argv[0]))


def parseAmxd(path):
    result = ""
    with open(path, "rb") as fileObj:
        encrypted = False
        while True:
            chunk = fileObj.read(4)
            if len(chunk) < 4:
                break

            field = chunk.decode("ascii")
            datasize = int.from_bytes(fileObj.read(4), byteorder="little")
            data = fileObj.read(datasize)

            if field == "ciph":
                encrypted = True

            if field == "ptch" and encrypted:
                result += "<Patch is encrypted>\n"
            else:
                result += parseField(field, datasize, data)
    return result


def parseField(field, datasize, data):
    result = ""
    if field == "ampf":
        if datasize != 4:
            print("Incorrect device type argument")
            sys.exit(2)
        devicetype = data.decode("ascii")
        if devicetype == "aaaa":
            result += "Audio Effect Device\n"
        elif devicetype == "mmmm":
            result += "MIDI Effect Device\n"
        elif devicetype == "iiii":
            result += "Instrument Device\n"
        elif devicetype == "nagg":
            result += "MIDI Tool Generator\n"
        elif devicetype == "natt":
            result += "MIDI Tool Transformation\n"
        else:
            result += "Unknown device type\n"
        result += "-------------------\n"
    elif field == "meta":
        result += ""  # unused
    elif field == "ciph":
        result += "----- Cipher -----\n"
        result += (
            "..." + data[datasize - 8 : datasize].hex() + "\n"
        )  # print last part of cipher to show if there is a difference
    elif field == "ptch":
        # only called if the device is not encrypted
        if data[:4].decode("ascii") == "mx@c":
            result += "Device is frozen"
        else:
            if data[datasize - 1] == 0:
                # json.loads doesn't like if there is a value of 0
                # at the end of the string which Max appears to add
                patcherDict = json.loads(data[: datasize - 1].decode("utf-8"))
            else:
                # but we also want to support if the JSON is written by JS.
                patcherDict = json.loads(data.decode("utf-8"))
            result += printPatcher(patcherDict)
    else:
        print("Unknown field", field)
        sys.exit(2)
    return result


if __name__ == "__main__":
    main(sys.argv[1:])
