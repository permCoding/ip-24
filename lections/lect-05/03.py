def isPalindrom(s):
    s = s.lower()
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    return True


# s = "Топор"
s = "А роза упала на лапу Азора."
pref = '' if isPalindrom(s) else 'не '
print(f'{s} - {pref}палиндром')




# print(s[0], ord(s[0]))
# print(s[-1], ord(s[-1]))

# a, b = input(), input()
# print(a > b)
