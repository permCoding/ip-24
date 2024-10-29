from math import pi

x = pi/6

d = -1
p = 3
q = x
f = 1
sin = x
while p <= 11:
    q *= x*x
    f *= (p-1)*p
    sin += d * q / f
    p += 2
    d = -d

print(sin)
