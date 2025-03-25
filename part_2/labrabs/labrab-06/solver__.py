lst = ['_'] + [line.split('\t')[1].strip('\n') for line in open('./people.csv').readlines()]
pairs = [[int(e) for e in line.split('\t')] for line in open('./refs.csv').readlines()]
print(len(set([e[1] for e in pairs if lst[e[0]] == lst[e[1]]])))
