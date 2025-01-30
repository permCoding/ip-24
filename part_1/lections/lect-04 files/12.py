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


lines = getLines('./docs/data.csv')
title = lines[0]
abiturs = getAbiturs(lines[1:])
avg = sum([x[-1] for x in abiturs]) / len(abiturs)
filtred = [x for x in abiturs if x[-1]>avg]


f_lines = [','.join([str(obj[0]),obj[1],str(obj[2])])+'\n' for obj in filtred]
with open('./f_abits.csv', 'w', encoding='utf8') as f:
    f.write(title)
    f.writelines(f_lines)
