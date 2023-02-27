import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, FormatStrFormatter

# FormatStrFormatter
# позволяет устанавливать формат числовых данных подписей рисок

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi / 2, np.pi, 0.1)

ax.plot(x, np.sin(x))
#ax.yaxis.set_major_formatter(FormatStrFormatter('%d')) # будет округлять все числа до целых и по оси Oy
#ax.yaxis.set_major_formatter(FormatStrFormatter('%f')) # получим вещественные числа с шестью знаками после запятой
#ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f')) # В данном случае мы ограничиваемся двумя цифрами после запятой
ax.yaxis.set_major_formatter(FormatStrFormatter('y = %.2f')) # перед каждым числом будет записано «y = »

ax.grid()
plt.show()