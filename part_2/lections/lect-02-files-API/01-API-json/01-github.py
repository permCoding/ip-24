import requests, json


user = 'permCoding'
url = f'https://api.github.com/users/{user}/repos'
repsonse = requests.get(url)
repsonse.encoding = "utf8"

lst = repsonse.json()  # ===
print(json.dumps(lst[0], indent=2, ensure_ascii=False))

# print(len(lst))
