import json
import sys

# Checking if the command line has arguments, and if yes,
# assign the argument to the variable for main func, otherwise print error
# Making the script portable by defining absolute path
with open("countries.json") as f:
    countries = json.load(f)

if len(sys.argv) == 2:
     key = sys.argv[1]
else:
    print("Incorrect parameter.")
    sys.exit()

# Defining a dynamic global list for error-checking related with unsupported user input
official_keys = []

# Filling in the global list defined above
for i in range(len(countries)):
    for j in countries[i]["translations"]:
        if j not in official_keys:
            official_keys.append(j)

# Main function that uses if-else statement to error-check and if none is triggered, translates country names
if key not in official_keys:
    print("Key is not supported!")
else:
    for i in range(len(countries)):
        if key in countries[i]["translations"]:
            print(countries[i]["translations"][key]["official"])
f.close()
