import matplotlib.pyplot as plt
import numpy as np


x1 = np.linspace(-2.0*np.pi, 0.2*np.pi, 101)
y1 = 1/2*np.sin(2*x1)

x2 = np.linspace(0.2*np.pi, 2.0*np.pi, 101)
y2 = np.sin(x2)

plt.plot(x1, y1, linewidth=3, color='green')
plt.plot(x2, y2, linewidth=3, color='red')

plt.axhline(linewidth=1, color='#22D')
plt.axvline(linewidth=1, color='#22D')

plt.xticks(np.linspace(-7.0, +7.0, 15))

plt.grid(True)

plt.show()
