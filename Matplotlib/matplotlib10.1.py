import numpy as np
import matplotlib.pyplot as plt

# Круговые диаграммы

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()

vals = [10, 40, 23, 30, 7]
labels = ['Toyota', 'BMW', 'Lexus', 'Audi', 'Lada']
ax.pie(vals, labels=labels)

plt.show()

# 2
fig2 = plt.figure(figsize=(6, 4))
ax2 = fig2.add_subplot()

vals2 = [10, 40, 23, 30, 7]
labels2 = ['Toyota', 'BMW', 'Lexus', 'Audi', 'Lada']
exp2 = (0.1, 0.2, 0, 0, 0)
ax2.pie(vals, labels=labels2, autopct='%.2f', explode=exp2, shadow=True)

plt.show()

# 3
fig3 = plt.figure(figsize=(6, 4))
ax3 = fig3.add_subplot()

vals3 = [10, 40, 23, 30, 7]
labels3 = ['Toyota', 'BMW', 'Lexus', 'Audi', 'Lada']
exp3 = (0.1, 0.2, 0, 0, 0)
ax3.pie(vals3, labels=labels3, shadow=True, wedgeprops=dict(width=0.5))

plt.show()


