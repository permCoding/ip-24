import matplotlib.pyplot as plt  # https://matplotlib.org/
import numpy as np


x = np.linspace(-2.5, 2.0*np.pi, 101)
y1 = np.sin(2*x)  # [math.sin(2*elm) for elm in x] 
y2 = 2/3*np.cos(x)

plt.plot(x, y1, 'green', x, y2, 'red')
plt.title('Графики функций')
plt.legend(['sin(2*x)', '2/3*cos(x)'])

plt.xlabel('-x-')
plt.ylabel('-y-')

plt.grid(False)  # это без сетки

plt.show()
