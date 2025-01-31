import matplotlib.pyplot as plt
import numpy as np

# x = [round(i/10, 6) for i in range(0, 101)]
x = np.linspace(0, 100, 101)
y = [elm**2 for elm in x]

plt.plot(x, y, color='green')
plt.title('График функции')
plt.legend(['y = x**2'])

plt.xlabel('-ось x-')
plt.ylabel('-ось y-')

plt.axis( [1, 9, -10.5, 85] )
plt.grid()

# plt.xticks(np.linspace(2,9,8))
plt.yticks(np.linspace(0,100,11))

plt.show()
