def isPalindrom(s):
    s = s.lower()
    
    return True


s = "Топот"
pref = '' if isPalindrom(s) else 'не '
print(f'{s} - {pref}палиндром')




# print(s[0], ord(s[0]))
# print(s[-1], ord(s[-1]))

# a, b = input(), input()
# print(a > b)
