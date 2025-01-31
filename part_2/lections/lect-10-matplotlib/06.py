import matplotlib.pyplot as plt  # https://matplotlib.org/
import numpy as np


x = np.linspace(-2.5, 2.0*np.pi, 101)
y1 = np.sin(2*x)
y2 = 2/3*np.cos(x)
y3 = np.sin(x) - np.cos(2*x)

styles = plt.style.available
print(styles)
# plt.style.use(styles[0])
plt.style.use('Solarize_Light2')

plt.plot(x, y1, linewidth=3, color='green', label='y1')
plt.plot(x, y2, color='red', label='y2')
plt.plot(x, y3, lw=4, color='#A2B', label='y3')
plt.legend()
# plt.legend(['y1', 'y2', 'y3'])
plt.title('Графики функций')

plt.xlabel('-x-')
plt.ylabel('-y-')

plt.axhline(linewidth=1, color='#22D')
plt.axvline(linewidth=1, color='#22D')

plt.grid(True)

plt.show()


# https://youtu.be/t3LloJzKiRE?si=QvgmOagFN9KOH_9G
# https://youtu.be/qLjHgUwLOrs?si=X_EQC1HwknGbXyyl