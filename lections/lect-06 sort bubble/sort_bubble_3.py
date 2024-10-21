def sort_bubble(t):  # N**2
    for j in range(0, len(t)-1):
        for i in range(0, len(t)-1-j):
            if t[i] > t[i+1]:
                t[i], t[i+1] = t[i+1], t[i]
    return t


def sort_bubble_opt(t):
    for j in range(0, len(t)-1):
        for i in range(0, len(t)-1-j):
            if t[i] > t[i+1]:
                t[i], t[i+1] = t[i+1], t[i]
    return t

t = [1, 2, 4, 6, 8]
t = [1, 2, 4, 8, 6]
print(t)

