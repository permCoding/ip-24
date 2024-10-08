def isPalindrom(s, q):
    s = ''.join(smb for smb in s.lower() if smb in q)
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    return True


alph = ''.join(str(i) for i in range(0, 10))
AZ = ''.join(chr(i) for i in range(65, 91))
alph += AZ + AZ.lower()
s = '- 123 000 321 !"@ '
# s = "А роза упала на лапу Азора."
print(f'{s} - {"" if isPalindrom(s, alph) else "не "}палиндром')
