from string import punctuation, whitespace


def isPalindrom(s):
    # def check(e): return (e not in punctuation) and (e not in whitespace)
    
    def check(e): 
        return not ((e in punctuation) or (e in whitespace))
    
    s = ''.join( smb for smb in s.lower() if check(smb) )
    d = len(s)//2
    return s[:d] == s[-d:][::-1]


s = "А роза упала на лапу Азора."
print(f'{s} - {"" if isPalindrom(s) else "не "}палиндром')
