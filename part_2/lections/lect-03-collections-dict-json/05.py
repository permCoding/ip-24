import json

s = """[
  {
    "id": 12,
    "name": "Федоров"
  },
  {
    "id": 8,
    "name": "Петров"
  }
]"""


objs = json.loads(s)

for obj in sorted(objs, key=lambda x: x["id"]):
    print(json.dumps(obj, ensure_ascii=False, indent=2))
