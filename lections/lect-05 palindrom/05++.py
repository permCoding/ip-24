def isPalindrom(s):
    s = ''.join(smb for smb in s.lower() if smb.isalnum())
    print(s)  # для контроля выбора разрешённых символов
    d = len(s)//2
    return s[:d] == s[-d:][::-1]


s = "А роза упала на лапу Азора."
print(f'{s} - {"" if isPalindrom(s) else "не "}палиндром')
