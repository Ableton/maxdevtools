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
    deviceTypes = {
        "aaaa": "Audio Effect Device",
        "mmmm": "MIDI Effect Device",
        "iiii": "Instrument Device",
        "nagg": "MIDI Tool Generator",
        "natt": "MIDI Tool Transformation",
    }

    fieldHandlers = {
        "ampf": handleAmpf,
        "meta": handleMeta,
        "ciph": handleCiph,
        "ptch": handlePtch,
    }

    if field in fieldHandlers:
        return fieldHandlers[field](datasize, data, deviceTypes)
    else:
        print(f"Unknown field {field}")
        sys.exit(2)


def handleAmpf(datasize, data, device_types):
    if datasize != 4:
        print("Incorrect device type argument")
        sys.exit(2)
    devicetype = data.decode("ascii")
    return f"{device_types.get(devicetype, 'Unknown device type')}\n-------------------\n"


def handleMeta(datasize, data, device_types):
    return ""


def handleCiph(datasize, data, device_types):
    return f"----- Cipher -----\n...{data[datasize-8:datasize].hex()}\n"


def handlePtch(datasize, data, device_types):
    if data[:4].decode("ascii") == "mx@c":
        return "Device is frozen"
    else:
        if data[datasize - 1] == 0:
            patcherDict = json.loads(data[: datasize - 1].decode("utf-8"))
        else:
            patcherDict = json.loads(data.decode("utf-8"))
        return printPatcher(patcherDict)


if __name__ == "__main__":
    main(sys.argv[1:])
