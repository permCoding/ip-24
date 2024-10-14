# s = []
# for i in range(1, 12):
#     if i**2 % 2 > 0:
#         s.append(i**2)

s = [ i**2 for i in range(1, 12) if i**2 % 2 > 0 ]
print(s)

