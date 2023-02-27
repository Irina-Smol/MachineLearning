import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator, IndexLocator

# IndexLocator
# производит отсчет значений рисок не от 0, а от наименьшего значения данных графика. В конструкторе класса IndexLocator определены два параметра:
# base – шаг изменения между соседними рисками;
# offset – смещение относительно наименьшего значения.

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.arange(-np.pi/2, np.pi, 0.1)
ax.plot(x, np.sin(x))

ax.grid()
ax.xaxis.set_major_locator(IndexLocator(base=0.5, offset=0))
plt.show()

ax.grid()
ax.xaxis.set_major_locator(IndexLocator(base=0.5, offset=0.57)) 
plt.show()