from itertools import groupby
import json

with open('./clients.json', 'r', encoding='utf8') as f:
    clients = json.load(f)['clients']

keys = ['id', 'age', 'gender', 'name']  # выбираем поля
new_clients = [{key: client[key] for key in keys} for client in clients]

new_clients.sort(key=lambda x: x['gender'])  # сортируем
grb = groupby(new_clients, key=lambda x: x['gender'])  # группируем

def get_sorted(gr):  # сортировка по двум параметрам последовательно
    srt_rev = sorted(list(gr), key=lambda x: x['name'], reverse=True)
    return sorted(srt_rev, key=lambda x: -x['age'])
lst = {key:get_sorted(gr) for key, gr in grb}

print( json.dumps(lst, indent=4, ensure_ascii=False) )
with open('./clients_.json', 'w', encoding='utf8') as f:
    json.dump(obj=lst, fp=f, indent=4, ensure_ascii=False)
