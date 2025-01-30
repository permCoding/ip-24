def bin_search(t, e, deep=0):
    l, r = 0, len(t)-1
    while l <= r:
        deep += 1
        m = (r+l)//2
        if e == t[m]: return m
        if e > t[m]: l = m+1
        else: r = m-1
    return -1, deep

lst = [1,2,6,9,13,15,17,18]
search_elm = 16
tpl = bin_search(lst, search_elm)
print(f"pos elm {search_elm}: {tpl[0]}; steps = {tpl[1]}")

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