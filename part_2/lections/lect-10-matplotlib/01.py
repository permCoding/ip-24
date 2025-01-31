# sudo apt install python3-numpy
# sudo apt -y install python3-matplotlib
# https://matplotlib.org/
# pip install numpy
# pip install matplotlib

import numpy as np

x = list(range(0, 11, 1))
print(x)

x = [elm/10 for elm in range(0, 101, 1)] 
print(x)

x = np.linspace(0, 10, 101)  # ver_1
print(x)

x = map(lambda elm: round(elm, 6), x)  # ver_2
print(list(x))

x = []  # ver_3
n, step = 0, 0.1
while n <= 10:
    # x.append(n)
    x.append(round(n,6))
    n += step
print(x)

"""
4 bit
0000 = 0
0001
0010
0011
0100
0101 = 5
0*2**3 + 1*2**2 + 0*2**1 + 1*2**0

0*8 + 1*4 + 0*2 + 1*1 = 5
125(10) = 1*100 + 2*10 + 5*1 = 125

3(10) => 00000000000000000011(2)
2 byte => 16 bit => 65356

.5(10) => . 1*2**-1 + 0*2**-2 ** 0*2**-3
1/2 1/4 1/8 1/16 1/32 ======>>>>>>>>>>>>>>>>>>>>>>> 1024

.101(2) => 1*2**-1 + 0 + 1*2**-3 (10)

"""