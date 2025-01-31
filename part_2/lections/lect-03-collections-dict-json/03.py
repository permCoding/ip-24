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

s = json.dumps(a, ensure_ascii=False, indent=4)
print(s)
