# MultipleLocator
# позволяет задавать шаг изменения значений между соседними рисками
# параметр base этого класса, который и определяет шаг следования значений в соответствии с формулой:
# base ∙ i,    где  i = ±1, ±2, ...

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator, IndexLocator

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.25))
ax.grid()
# ax.xaxis.set_major_locator(MultipleLocator(base=3.5))
plt.show()

# IndexLocator
# производит отсчет значений рисок не от 0, а от наименьшего значения данных графика. В конструкторе класса IndexLocator определены два параметра:
# base – шаг изменения между соседними рисками;
# offset – смещение относительно наименьшего значения.

x = np.arange(-np.pi/2, np.pi, 0.1)
ax.plot(x, np.sin(x))

ax.grid()
ax.xaxis.set_major_locator(IndexLocator(base=0.5, offset=0))
