def to_float(line):
    return float(
        line
            .split(';')[0]
            .replace(',','.')
            .replace('%','')
    )


def to_lang(line):
    return line.split(';')[1].replace('\n','')


def get_tpl(line):
    return (to_float(line), to_lang(line))


lines = [line for line in open('./input-3.txt')]
langs = [get_tpl(line) for line in lines]
for tpl in sorted(langs, key=lambda elm: elm[1]):
    print(*tpl)
