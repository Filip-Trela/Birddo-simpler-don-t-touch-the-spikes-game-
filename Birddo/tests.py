#for highscore

import json

#with open("Saves.py", "w") as outfile:
#    json.dump(dictionary, outfile)

with open('Saves.py', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object["highscore"])
