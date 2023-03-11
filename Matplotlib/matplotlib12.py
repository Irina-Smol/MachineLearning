import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(7, 4))
ax_3d = fig.add_subplot(projection='3d')

plt.show()

# 2
fig2 = plt.figure(figsize=(7, 4))
ax_3d2 = fig2.add_subplot(projection='3d')

x = np.linspace(0, 10, 50)
z = np.cos(x)
ax_3d2.plot(x, x, z)

plt.show()

