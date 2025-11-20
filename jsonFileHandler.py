import json

def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file, you must check again for name file in directory Files")
    return data
    
# Memanggil fungsi
myJsonFile = readJsonFile("files/insulin.json")
if (myJsonFile != ""):
    print("Your file json it's works")
    #rint(myJsonFile)
else:
    print("This is error")
#print(myJsonFile["molecularWeightInsulinActual"])