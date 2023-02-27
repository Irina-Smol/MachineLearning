import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator, IndexLocator, FixedLocator, LogLocator, MaxNLocator

# set_minor_locator()
# Все те же самые действия можно выполнять и с мелкой (минорной) сеткой. Для этого ее нужно сначала включить и показать на графике:
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.arange(-np.pi/2, np.pi, 0.1)
ax.plot(x, np.sin(x))

ax.minorticks_on()
ax.grid(which='major', lw = 2) # параметр which функции grid() как раз указывает какую сетку показать
ax.grid(which='minor')

ax.xaxis.set_minor_locator(NullLocator())
plt.show()