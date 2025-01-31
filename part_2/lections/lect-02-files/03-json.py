import json

f = open('./data/users.json')
arr = json.load(f)
f.close()

# print(arr)

# print(arr[0])

print(json.dumps(arr[0], indent=2))

