def ex_01(string):
    for ind in range(0, len(string)):
        smb = string[ind]
        print(smb, ord(smb))

def ex_02(string):
    for smb in string:
        print(smb, ord(smb))


f = open('./01.py')
string = f.read()
f.close()
ex_02(string)
