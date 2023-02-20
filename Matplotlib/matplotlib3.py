import matplotlib.pyplot as plt
import numpy as np

# Отображение нескольких координатных осей в одном окне
# subplot(nrows, ncols, index) где nrows, ncols – число строк и столбцов; index – индекс текущих координатных осей

# 1
plt.subplot(1, 3, 1)
plt.plot(np.random.random(10))
plt.subplot(1, 3, 2)
plt.plot(np.random.random(10))
plt.subplot(1, 3, 3)
plt.plot(np.random.random(10))
plt.grid()
plt.show()

# 2
ax1 = plt.subplot(1, 3, 1)
plt.plot(np.random.random(10))
ax2 = plt.subplot(1, 3, 2)
plt.plot(np.random.random(10))
ax3 = plt.subplot(1, 3, 3)
plt.plot(np.random.random(10))
ax1.grid()
ax2.grid()
ax3.grid()
plt.show()

# 3
ax1 = plt.subplot(2, 3, 1)
plt.plot(np.random.random(10))
ax2 = plt.subplot(2, 3, 2)
plt.plot(np.random.random(10))
ax3 = plt.subplot(2, 3, 3)
plt.plot(np.random.random(10))
ax4 = plt.subplot(2, 1, 2)
plt.plot(np.random.random(10))
plt.show()

# 4 если nrows < 10 и ncols < 10, то вместо трех чисел можно указывать одно трехзначное число
ax6 = plt.subplot(131)
plt.plot(np.random.random(10))
ax7 = plt.subplot(132)
plt.plot(np.random.random(10))
ax5 = plt.subplot(133)
plt.plot(np.random.random(10))

# Функция subplots()
# subplots(nrows, ncols)

# 5
f, ax = plt.subplots(2, 2)
plt.show()

ax[0, 0].plot(np.arange(0, 5, 0.2))
ax[0, 0].grid()
ax[0, 1].plot(np.arange(5, 0, -0.2))
ax[0, 1].grid()
plt.show() # 6

# Объект Figure

fig = plt.figure(figsize=(7, 4))
plt.plot(np.arange(0, 5, 0.2))
plt.show() # 7



