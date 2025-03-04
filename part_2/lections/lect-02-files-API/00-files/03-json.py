import json

f = open('./data/users.json')
lst = json.load(f)
f.close()

# print(lst)

# print(lst[0])

print(json.dumps(lst[0], indent=2))
