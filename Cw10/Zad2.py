import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 20)

plt.plot(x, 1/x, 'g:>', label='f(x) = 1/x')

plt.xlabel('x')
plt.ylabel('f(x)')

plt.xlim(0, 20)
plt.ylim(0, 1)

plt.title("Wykres funkcji f(x) dla x [1, 20]")

plt.legend()

plt.show()
