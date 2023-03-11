import numpy as np
import matplotlib.pyplot as plt

# Гистограмма и столбчатые диаграммы

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()

y = np.random.normal(0, 2, 500)
ax.hist(y)
ax.grid()

plt.show()

# 2
fig2 = plt.figure(figsize=(6, 4))
ax2 = fig2.add_subplot()

y2 = np.random.normal(0, 2, 500)
ax2.hist(y, 50)
ax2.grid()

plt.show()

# 3
fig3 = plt.figure(figsize=(6, 4))
ax3 = fig3.add_subplot()

x3 = [f'H{i+1}' for i in range(10)]
y3 = np.random.randint(1, 5, len(x3))
ax3.bar(x3, y3)
ax3.grid()

plt.show()

# 4
fig4 = plt.figure(figsize=(6, 4))
ax4 = fig4.add_subplot()
# сформируем сами величины и разобьем весь интервал на 10 равных диапазонов
y4 = np.random.normal(0, 2, 500)
x4 = np.linspace(np.min(y4), np.max(y4), 10)
# подсчитаем, сколько величин попало в соответствующий диапазон и выведем список bars с помощью функции bar()
bars = [len(y4[np.bitwise_and(y4 >= x4[i], y4 < x4[i+1])]) for i in range(len(x4)-1)]
ax4.bar(range(len(x4)-1), bars)
ax4.grid()

plt.show()

# Если нужно отображать столбики относительно оси ординат, то для этого существует функция barh(), которая работает аналогично функции bar():
# ax.barh(range(len(x)-1), bars)

# 5
fig5 = plt.figure(figsize=(6, 4))
ax5 = fig5.add_subplot()

x5 = [f'H{i+1}' for i in range(10)]
y5 = np.random.randint(-20, 20, len(x5))
ax5.bar(x5, y5, width=0.5, linewidth=2, edgecolor='r', yerr=2, bottom=10)
ax5.grid()

plt.show()

# 6
fig6 = plt.figure(figsize=(6, 4))
ax6 = fig6.add_subplot()

x6 = np.arange(10)
y7 = np.random.randint(3, 20, len(x6))
y8 = np.random.randint(3, 20, len(x6))
w = 0.3
ax6.bar(x6 - w/2, y7, width=w)
ax6.bar(x6 + w/2, y8, width=w)
ax6.grid()

plt.show()
