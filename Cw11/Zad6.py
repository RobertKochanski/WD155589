import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()

ax = plt.subplot(121, projection="3d")
x = 10 * np.random.rand(20)
y = 10 * np.random.rand(20)
z = 10 * np.random.rand(20)
ax.scatter(x, y, z, c="b", marker=".")

ax = plt.subplot(122, projection="3d")
x = 10 * np.random.rand(5)
y = 10 * np.random.rand(5)
z = 10 * np.random.rand(5)
ax.plot(x, y, z, c="r")

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
