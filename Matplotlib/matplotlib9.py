import numpy as np
import matplotlib.pyplot as plt


# Ступенчатый (step) график

# 1

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()

x = np.arange(0, 10)
# ax.step(x, x)
ax.step(x, x, '-go')
ax.grid()

plt.show()

# 2
fig2 = plt.figure(figsize=(4, 4))
ax2 = fig2.add_subplot()

x2 = np.arange(0, 10)
ax2.step(x, x, '-go', where='post') # where = {'pre',  'post',  'mid'}, where='mid' отсчеты располагаются по центрам ступенек.
ax2.grid()

plt.show()

# 3
fig3 = plt.figure(figsize=(4, 4))
ax3 = fig3.add_subplot()

x3 = np.arange(0, 10)
ax3.step(x, x, '-go', x, np.cos(x), '--x', where='mid')  # создавать несколько таких графиков в пределах одной системы координат

plt.show()

