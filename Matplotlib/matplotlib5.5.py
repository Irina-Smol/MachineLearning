import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, FormatStrFormatter, FuncFormatter, ScalarFormatter

# ScalarFormatter
# отображает числовые данные так, как они есть с небольшими манипуляциями.
# Если число оказывается очень большим (больше 10^10), то его множитель выносится

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi / 2, np.pi, 0.1)

ax.plot(x, np.sin(x) * 1e5)

sf = ScalarFormatter()
sf.set_powerlimits((-4, 4)) # указать максимальную и минимальную степень 4
ax.yaxis.set_major_formatter(sf)  # степень 10^5 была вынесена за скобки


ax.grid()
plt.show()