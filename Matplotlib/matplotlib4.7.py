import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator, IndexLocator, FixedLocator, LogLocator, MaxNLocator

# MaxNLocator
# выполняет самостоятельную разбивку интервала на число рисок не более значения nbins, указанного при создании его экземпляра

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.arange(-np.pi/2, np.pi, 0.1)
ax.plot(x, np.sin(x))

ax.grid()
#ax.xaxis.set_major_locator(MaxNLocator())
plt.show()


# зададим максимальное число рисок, равное пяти:
ax.grid()
ax.xaxis.set_major_locator(MaxNLocator(nbins=5))
plt.show()