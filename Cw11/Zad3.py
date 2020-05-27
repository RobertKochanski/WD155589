import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

X = np.arange(- 5, 5, 0.25)
Y = np.arange(- 5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

ax = plt.subplot(321, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap=cm.jet, linewidth=0, antialiased=False)
ax.set_zlim(- 1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
plt.colorbar(surf, shrink=0.5, aspect=5)

ax = plt.subplot(322, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_rainbow, linewidth=0, antialiased=False)
ax.set_zlim(- 1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
plt.colorbar(surf, shrink=0.5, aspect=5)

ax = plt.subplot(323, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap=cm.brg, linewidth=0, antialiased=False)
ax.set_zlim(- 1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
plt.colorbar(surf, shrink=0.5, aspect=5)

ax = plt.subplot(324, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap=cm.flag, linewidth=0, antialiased=False)
ax.set_zlim(- 1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
plt.colorbar(surf, shrink=0.5, aspect=5)

ax = plt.subplot(325, projection="3d")
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax.set_zlim(- 1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
plt.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
