with open('./docs/data_2.csv', encoding='utf8') as f:
    lines = []
    for line in f.readlines():
        if ord(line[-1]) == '10':
            lines.append(line[:-1])
        else:
            lines += [line]
print(lines)
