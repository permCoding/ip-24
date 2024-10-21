from random import randint as rnd


n = 1_000

lst_1 = [rnd(1, 10_000) for _ in range(n)]

lst_2 = sorted([rnd(1, 10_000) for _ in range(n//2)])
lst_2 += [rnd(1, 10_000) for _ in range(n//2)]

lst_3 = sorted([rnd(1, 10_000) for _ in range(n)])
for _ in range(n//20):
    left, right = rnd(n//2, n-1), rnd(n//2, n-1)
    lst_3[left], lst_3[right] = lst_3[right], lst_3[left]


print(lst_1)
print(lst_2)
print(lst_3)

