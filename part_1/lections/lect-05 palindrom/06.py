def isPalindrom(s):
    if len(s) <= 1: return True
    return False if s[0] != s[-1] else isPalindrom(s[1:-1])


s = "А роза упала на лапу Азора!...."
s = ''.join(smb for smb in s.lower() if smb.isalnum())
print(f'{s} - {"" if isPalindrom(s) else "не "}палиндром')
