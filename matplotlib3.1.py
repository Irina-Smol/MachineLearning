import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(7, 4))
ax9 = fig.add_axes([0.0, 0, 1.0, 1.0])
ax9.plot(np.arange(0, 5, 0.2))
plt.show() # 8

fig = plt.figure(figsize=(7, 4))
ax9 = fig.add_subplot(1, 3, 1)
ax9.plot(np.arange(0, 5, 0.2))
plt.show() # 9

a, bx = plt.subplots() # создать окно с одной или несколькими осями
plt.show() # 10


# Компоновка графиков с помощью GridSpec

# Для более сложных элементов компоновки хорошо подходит класс GridSpec из ветки: matplotlib.gridspec

fig = plt.figure(figsize=(7, 4))
gs = GridSpec(ncols=3, nrows=2, figure=fig)

ax1 = plt.subplot(gs[0, 0])
ax1.plot(np.arange(0, 5, 0.2))
ax2 = fig.add_subplot(gs[1, 0:2])
ax2.plot(np.random.random(10))
ax3 = fig.add_subplot(gs[:, 2])
ax3.plot(np.random.random(10))
plt.show()

# можно задавать размеры каждого графика (относительно суммарной длины всех ячеек) в виде списков
ws = [1, 2, 5]
hs = [2, 0.5]

fig = plt.figure(figsize=(7, 4))
gs = GridSpec(ncols=3, nrows=2, figure=fig, width_ratios=ws, height_ratios=hs)
ax1 = plt.subplot(gs[0, 0])
ax1.plot(np.arange(0, 5, 0.2))
ax2 = fig.add_subplot(gs[1, 0:2])
ax2.plot(np.random.random(10))
ax3 = fig.add_subplot(gs[:, 2])
ax3.plot(np.random.random(10))
plt.show() # 5