import json
import sys
from sys import argv


#access .json file and load it's insides
with open('countries.json') as f:
    countries = json.load(f)

#create a list of translation keys from .json file
official_keys = {}
for c in countries:
    official_keys.setdefault(c['name']['official'], {}).update(c['translations'])

#check if key value is empty or more than 1 s
if len(sys.argv) == 1 or len(sys.argv) > 2:
    print("Incorrect parameter")
    sys.exit()
else:
    key = argv[1]

#return countries names if CLI pAarameter matches one of the keys
for official, keys  in official_keys.items():
    if (key in keys):
        print(keys[key]["official"])
    else : 
        print ("Translation key is not supported")

f.close()
