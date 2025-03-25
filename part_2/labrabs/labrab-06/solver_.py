lst = ['_'] + [line.split('\t')[1].strip('\n') for line in open('./people.csv').readlines()]

res = set()
for line in open('./refs.csv').readlines():
    tpl = [int(e) for e in line.split('\t')]
    if lst[tpl[0]] == lst[tpl[1]]:
        res.add(tpl[1])

print(len(res))
