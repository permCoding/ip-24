import json

f = open("./pogoda.json")
data = json.load(f)
print(data)
