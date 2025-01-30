# for
# while
# if
# def

# lst = list(1,2,3) 
lst = [99,1,2,3,4,5,6,777]
print(lst)
print(*lst)
print(lst[0])
for i in range(len(lst)):
    print(i, lst[i])

i = 0
while i < len(lst):
    print(i, lst[i])
    i += 1

s = '01234567'