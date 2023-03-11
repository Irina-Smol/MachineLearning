import numpy as np
import matplotlib.pyplot as plt

# Stem-график

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

x = np.arange(-np.pi, np.pi, 0.3)
ax.stem(x, np.cos(x))
ax.grid()

plt.show()

# По умолчанию уровень базовой линии находится в нуле. Но мы можем его изменить, указав значение через параметр bottom:
# ax.stem(x, np.cos(x), bottom=0.5)

# 2
fig2 = plt.figure(figsize=(4, 4))
ax2 = fig2.add_subplot()

x2 = np.arange(-np.pi, np.pi, 0.3)
ax2.stem(x, np.cos(x), bottom=0.5)
ax2.grid()

plt.show()
# Также третьим аргументом (или параметром linefmt) можно устанавливать тип и цвет линии
# ax.stem(x, np.cos(x), '--r', bottom=0.5)
# А четвертым – тип и цвет маркеров (или же с помощью параметра markerfmt):
# ax.stem(x, np.cos(x), '--r', '^g', bottom=0.5)
