from itertools import groupby
# groupby требует, чтобы данные были отсортированы 
# по ключу, по которому вы собираетесь группировать.
import json

f = open('./clients.json', 'r', encoding='utf8')
clients = json.load(f)['clients']
# print(json.dumps(clients, indent=4, ensure_ascii=False))

clients.sort(key=lambda x: x['gender'])
grb = groupby(clients, key=lambda x: x['gender'])
# for key, gr in grb: print(key)
# for key, gr in grb:
#     t = list(gr)
#     print(key, t, len(t))

lst = {key:sorted(list(gr), key=lambda x: (-x['age'],x['name'])) for key, gr in grb}
s_json = json.dumps(lst, indent=4, ensure_ascii=False)
print(s_json)
    