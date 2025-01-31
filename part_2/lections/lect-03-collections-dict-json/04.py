import json

def get_objs():
    a = {}
    a["id"] = 12
    a["name"] = "Федоров"

    lst = [
        ("id", 8),
        ("name", "Петров")
    ]
    b = dict(lst)
    return a, b


a, b = get_objs()

lst = [a, b]
s = json.dumps(lst, ensure_ascii=False, indent=4)
print(s)

with open(file="./json/objs.json", mode="w", encoding="utf8") as f:
    json.dump(lst, f, ensure_ascii=False, indent=2)
