from random import randint as rnd
from timeit import default_timer as dt

def line_search(t, e):
    for i in range(len(t)):
        if e == t[i]:
            return i, i+1
    return -1

def bin_search(t, e, deep=0):
    l, r = 0, len(t)-1
    while l <= r:
        deep += 1
        m = (r+l)//2
        if e == t[m]: return m, deep
        if e > t[m]: l = m+1
        else: r = m-1
    return -1, deep

def rec_search(e, l, r):
    if l > r: return -1, 0  # точка останова 1
    m = (r+l)//2
    if e == lst[m]: return m, 0  # точка останова 2
    if e > lst[m]: return rec_search(e, m+1, r)  # шаг 1
    else: return rec_search(e, l, m-1)  # шаг 2


lst = sorted(rnd(1, 1_000_000) for _ in range(1_000_000))
search_elm = lst[666_666]

st = dt()
pos, steps = bin_search(lst, search_elm)
fi = dt()
print(f"pos elm {search_elm}: {pos}; steps = {steps}")
print(round(fi-st, 3))

st = dt()
pos, steps = line_search(lst, search_elm)
fi = dt()
print(f"pos elm {search_elm}: {pos}; steps = {steps}")
print(round(fi-st, 3))

st = dt()
pos, steps = rec_search(search_elm, 0, len(lst)-1)
fi = dt()
print(f"pos elm {search_elm}: {pos}; steps = {steps}")
print(round(fi-st, 3))






"""
1_000_000
АссСл = O(n**2)
АссСл = O(n*log(N))
АссСл = O(n)
"""


"""
- линейный  
- бинарный  
- бинарный рекурсивно  
- интерполяционный  
"""