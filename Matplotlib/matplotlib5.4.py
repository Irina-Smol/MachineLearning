import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, FormatStrFormatter, FuncFormatter

# FuncFormatter
# формирует значения на основе заданной функции
def formatOy(x, pos):
    return f"[{x}]" if x < 0 else f"({x})" # помечает отрицательные значения в квадратные скобки, положительные - в круглые

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi / 2, np.pi, 0.1)

ax.plot(x, np.sin(x))
ax.yaxis.set_major_formatter(FuncFormatter(formatOy))

ax.grid()
plt.show()