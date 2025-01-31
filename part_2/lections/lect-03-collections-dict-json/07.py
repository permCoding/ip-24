import json
import requests

url = "http://files-pcoding.1gb.ru/json?filename=clients.json"
resp = requests.get(url)
resp.encoding = "utf8"
objs = resp.json()

clients = objs["clients"]

for client in sorted(clients, key=lambda x: x["age"]):
    print(json.dumps(client, ensure_ascii=False, indent=2))
