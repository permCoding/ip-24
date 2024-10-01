with open('./docs/data.csv', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')
