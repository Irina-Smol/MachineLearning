import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

# set_xticklabels(), set_yticklabels() убрать числовые значения на координатных осях


fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi / 2, np.pi, 0.1)
ax.plot(x, np.sin(x))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid()
plt.show()

