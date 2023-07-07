import json
import numpy as np
import kender

# F U N C T I O N S

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)

# T E S T S

path = './'
filename = "example"
data = {}
data["kender"] = "huevos"
data["celipito"] = "live"

writeToJSONFile(path, filename, data)

input()