# всплытие только одного пузырька
t = [9, 2, 4, 6, 2]
print(t)

for i in range(0, len(t)-1):
    if t[i] > t[i+1]:
        t[i], t[i+1] = t[i+1], t[i]

print(t)

for i in range(0, len(t)-2):
    if t[i] > t[i+1]:
        t[i], t[i+1] = t[i+1], t[i]

print(t)

for i in range(0, len(t)-1):
    if t[i] > t[i+1]:
        t[i], t[i+1] = t[i+1], t[i]

print(t)

# 0   9 2 4 6 2   }   swap
# 1   2 9
# 2   2 4 9 
# 3   2 4 6 9
# 4   2 4 6 2 9   }    len-1 < = max elm

# 0   2 4 6 2 } 9
# 1   2 4
# 2   2 4 6
# 3   2 4 2 6 } 9

# 0   2 4 2 } 6 9


# 0  2 2 } 4 6 9

# 0 ----