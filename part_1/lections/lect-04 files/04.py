with open('./docs/data.csv', encoding='utf8') as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line[:-1])
