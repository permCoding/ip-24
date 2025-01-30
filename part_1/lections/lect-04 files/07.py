with open('./docs/data.csv', encoding='utf8') as f:
    lines = [line for line in f][1:]
# print(lines)

lst = lines[0].split(',')

print(lst[2], 2*lst[2])

rate = int(lst[2])

print(rate, 2*rate)
