with open('./docs/data.csv', encoding='utf8') as f:
    lines = [line for line in f][1:]

abiturs = []
for line in lines:
    t = line.split(',')
    abit = [int(t[0]), t[1], int(t[2])]
    abiturs.append(abit)

filtred = []
for abit in abiturs:
    if abit[2] < 200:
        filtred.append(abit)
print(filtred)

# {
#     'id': 12,
#     'name': "wkqgd2hqj",
#     'rate': 186
# }