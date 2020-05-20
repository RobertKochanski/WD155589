import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30, 0.1)
s = np.sin(x)+2
s2 = np.sin(x)*(-1)

plt.plot(x, s, label='sin(x)')
plt.plot(x, s2, label='sin(x)')

plt.xlabel('x')
plt.ylabel('sin(x)')

plt.title("Wykres sin(x), sin(x)")

plt.legend()

plt.show()