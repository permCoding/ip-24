def isPalindrom(s, q):
    e = s.lower()
    s = ''
    for smb in e:
        if smb not in q:
            s += smb
    print(s)
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    return True


q = ' -.!,"'

# s = "Топор"
s = "А роза упала на лапу Азора."
print(f'{s} - {"" if isPalindrom(s, q) else "не "}палиндром')
