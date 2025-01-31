import matplotlib.pyplot as plt  # https://matplotlib.org/
import numpy as np


x = np.linspace(-2.5, 2.0*np.pi, 101)
y1 = np.sin(2*x)
y2 = 2/3*np.cos(x)

styles = plt.style.available
print(styles)
plt.style.use(styles[0])

plt.plot(x, y1, 'green', x, y2, 'red')
plt.title('Графики функций')
plt.legend(['sin(2*x)', '2/3*cos(x)'])

plt.xlabel('-x-')
plt.ylabel('-y-')

plt.axhline(linewidth=3, color='#22D')
plt.axvline(linewidth=5, color='#22D')

plt.grid(True)

plt.show()


# https://youtu.be/t3LloJzKiRE?si=QvgmOagFN9KOH_9G
# https://youtu.be/qLjHgUwLOrs?si=X_EQC1HwknGbXyyl