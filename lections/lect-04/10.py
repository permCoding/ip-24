def getAbiturs(lines):
    abiturs = []
    for line in lines:
        t = line.split(',')
        abit = [int(t[0]), t[1], int(t[2])]
        abiturs.append(abit)
    return abiturs


def getLines(filename, sep=0):
    with open(filename, encoding='utf8') as f:
        return [line for line in f][sep:]


lines = getLines('./docs/data.csv', 1)
abiturs = getAbiturs(lines)

print(min(abiturs, key=lambda x: x[2]))

