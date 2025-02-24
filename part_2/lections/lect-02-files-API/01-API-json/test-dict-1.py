import json

dct = {
    '1': "пн",
    '2': "вт"
}


print(dct['1'])
dct['3'] = 'ср'

print(dct)

dict_to_str = json.dumps(dct, indent=4, ensure_ascii=False)
print(dict_to_str)

print(dct.items())
print(list(dct.keys()))
print(list(dct.values()))

keys = ['R', 'G', 'B']

dct = dict.fromkeys(keys, '#000000')
print(dct)

values = ['#FF0000', '#00FF00', '#0000FF']
zp = list(zip(keys, values))
print(zp)

dct = dict(zip(keys, values))
print(dct)

# with open("./test-dict.json", "w", encoding="utf8") as file_json:
#     json.dump(dct, file_json, ensure_ascii=False, indent=4)

with open('./test-dict.json', 'r', encoding='utf8') as file_json:
    dct = json.load(file_json)
    sorted_dict = {key: dct[key] for key in sorted(dct.keys())}
    print(sorted_dict)
