# set()
# list()
# tuple()
# dict()
import json


dct = dict()
dct = {}
dct['price'] = 1_000
print(dct)

dct = {
    'id': 1024,
    'nameBook': 'Моя первая книга'
}
print(dct)

lst = []
lst = list()

keys = ['price', 'link', 'nameBook']
data = [1500, 'http//owqidqh', 'Моя книга']

dct = {
    'price': data[0],
    'link': data[1],
    'nameBook': data[2]
}
lst.append(dct)
lst.append(dct)
print(lst)

s = json.dumps(lst, indent=4, ensure_ascii=False)
print(s)

filename = './books.json'
with open(filename, 'w', encoding='utf8') as f:
    json.dump(lst, f, indent=4, ensure_ascii=False)

lst = []
zp = zip(keys, data)
# print(list(zp))
dct = dict(zip(keys, data))
lst.append(dct)
print(lst)
