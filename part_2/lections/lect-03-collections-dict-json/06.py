import json


f = open("./json/clients.json", "r", encoding="utf8")
objs = json.load(f)

for obj in sorted(objs, key=lambda x: x["name"], reverse=True):
    print(json.dumps(obj, ensure_ascii=False, indent=2))
