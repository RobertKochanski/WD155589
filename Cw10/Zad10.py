import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# z zadania 2
plt.subplot(121)

x = np.arange(1, 20)

plt.plot(x, 1/x, 'g:>', label='f(x) = 1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(0, 20)
plt.ylim(0, 1)
plt.legend()

plt.annotate('punkt: x = 2, y = 1/x',
            xy=(2, 0.5), xycoords='data',
            xytext=(125, 20), textcoords='offset points',
            arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')


# z zadania 4
plt.subplot(122)

x = np.arange(0, 30, 0.1)
s = np.sin(x)+2
s2 = np.sin(x)*(-1)

plt.plot(x, s, label='sin(x)')
plt.plot(x, s2, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()


plt.annotate('punkt: x = 4.5, y = 1',
            xy=(4.5, 1), xycoords='data',
            xytext=(-70, 30), textcoords='offset points',
            arrowprops=dict(arrowstyle="->"),
            horizontalalignment='left', verticalalignment='bottom')

plt.show()