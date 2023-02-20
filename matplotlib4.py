import matplotlib.pyplot as plt
import numpy as np

# Граничные значения осей и локаторы для расположения меток на них

# Для существующих осей (после их создания) настройка граничных значений производится с помощью метода set, следующим образом:
# ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.25))
ax.set(xlim=(-5, 30), ylim=(-1, 6))
plt.xlim(-1, 20)
plt.ylim(-1, 6)

plt.show()

