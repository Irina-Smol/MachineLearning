import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

# NullFormatter
# позволяет отключать надписи под рисками у выбранной оси

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
x = np.arange(-np.pi / 2, np.pi, 0.1)

ax.plot(x, np.sin(x))
ax.xaxis.set_major_formatter(NullFormatter()) # подписи у оси ОХ пропали
ax.grid()
plt.show()

# По аналогии, можно работать и с осью ординат, только для этого следует использовать объект yaxis:
# ax.yaxis.set_major_formatter(NullFormatter())