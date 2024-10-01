with open('./docs/data.csv', encoding='utf8') as f:
    lines = [line[0:-1] for line in f.readlines()]
print(lines[1:])
