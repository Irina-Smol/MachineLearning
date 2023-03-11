import numpy as np
import matplotlib.pyplot as plt

# Точечный график

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

x = np.random.normal(0, 2, 500)
y = np.random.normal(0, 2, 500)
ax.scatter(x, y) # множество точек с этими случайными координатами можно отобразить с помощью функции scatter()
ax.grid()

plt.show()


# 2
fig2 = plt.figure(figsize=(4, 4))
ax2 = fig2.add_subplot()

x2 = np.random.normal(0, 2, 500)
y2 = np.random.normal(0, 2, 500)
ax2.scatter(x, y, s=50, c='g', linewidths=1, marker='s', edgecolors='r')
ax2.grid()

plt.show()
