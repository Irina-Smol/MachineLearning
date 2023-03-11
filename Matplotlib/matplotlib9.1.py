import numpy as np
import matplotlib.pyplot as plt

# Стековый график

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

x = np.arange(-2, 2, 0.1)
y1 = np.array([-y**2 for y in x]) + 8
y2 = np.array([-y**2 for y in x]) + 8
y3 = np.array([-y**2 for y in x]) + 8
ax.stackplot(x, y1, y2, y3)

plt.show()
