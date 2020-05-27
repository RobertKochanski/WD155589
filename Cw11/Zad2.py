import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

for c, m in [('r', 'o'), ('g', '^'), ('b', 'X'), ('black', 'D'), ('yellow', '1')]:
    x = 100 * np.random.rand(10)
    y = 100 * np.random.rand(10)
    z = 100 * np.random.rand(10)
    ax.scatter(x, y, z, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
