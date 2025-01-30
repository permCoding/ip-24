from random import randint as rnd
from timeit import default_timer as dt


def sort_bubble(t):  # N**2
    for j in range(0, len(t)-1):
        for i in range(0, len(t)-1-j):
            if t[i] > t[i+1]:
                t[i], t[i+1] = t[i+1], t[i]
    return t


n = 2_000

t = [rnd(1, 10_000) for _ in range(n)]

st = dt()

sort_bubble(t)

fi = dt()

print(round(fi-st, 2))
