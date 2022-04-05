import json
import sys

# access .json file and load it's insides
with open("countries.json") as f:
    countries = json.load(f)

# check if key value is empty or more than 1
if len(sys.argv) == 2:
    key = sys.argv[1]
else:
    print("Incorrect parameter.")
    sys.exit()

# create a list of translation keys from .json file
official_keys = []
for i in range(len(countries)):
    for j in countries[i]["translations"]:
        if j not in official_keys:
            official_keys.append(j)

# return countries names if CLI parameter matches one of the keys
if key not in official_keys:
    print("Key is not supported!")
else:
    for i in range(len(countries)):
        if key in countries[i]["translations"]:
            print(countries[i]["translations"][key]["official"])
f.close()
