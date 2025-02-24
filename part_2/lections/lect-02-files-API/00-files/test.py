def ex_01():
    s = "12345"
    mp = map(lambda x: x*9, list(s))
    # for elm in mp:
    #     print(elm)

    print(list(mp))


def ex_02():
    lst = ['60', '66', '100', '99', '9']
    lst.sort(key=lambda x: int(x))
    print(lst)

# ex_01()
ex_02()
