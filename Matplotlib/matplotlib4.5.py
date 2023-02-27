import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator, IndexLocator, FixedLocator

# FixedLocator
# устанавливает метки в указанных значениях

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.arange(-np.pi/2, np.pi, 0.1)
ax.plot(x, np.sin(x))

ax.grid()
ax.xaxis.set_major_locator(FixedLocator([-2, -1, 0, 1, 2, 3]))
plt.show()