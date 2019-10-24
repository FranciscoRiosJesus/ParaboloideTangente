
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = x**2 + y**2

# Plot the surface
ax.plot_surface(x, y, z, color='b')

a = 2
b = 2

z = 2*a*x + 2*b*y - a**2 - b**2

ax.plot_surface(x, y, z, color='g')

plt.show()
