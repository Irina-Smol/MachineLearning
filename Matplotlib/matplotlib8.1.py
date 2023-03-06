import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import *

l1 = Line2D([1, 2, 3], [1, 2, 3])

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
line, = ax.plot(np.arange(0, 5, 0.25), '--o', label='line1')
line, = ax.plot(np.arange(0, 10, 0.5), ':s', label='line2')
ax.add_line(l1)

plt.show()

# 2
l2 = Line2D([1, 2, 3], [1, 2, 3])

fig2 = plt.figure(figsize=(7, 4))
ax2 = fig2.add_subplot()
line2, = ax.plot(np.arange(0, 5, 0.25), '--o', label='line1')
line2, = ax.plot(np.arange(0, 10, 0.5), ':s', label='line2')
ax2.add_line(l2)
ax2.set(xlim=(1, 3), ylim=(1, 3))

plt.show()

# 3
x = np.arange(-2*np.pi, 2*np.pi, 0.1)
cos = Line2D(x, np.cos(x))

fig3 = plt.figure(figsize=(7, 4))
ax3 = fig3.add_subplot()

ax3.add_line(cos)
ax3.set(xlim=(-2*np.pi, 2*np.pi), ylim=(-1, 1))

plt.show()

# 4
x2 = np.arange(-2*np.pi, 2*np.pi, 0.1)
cos2 = Line2D(x, np.cos(x))

rect = Rectangle((0, 0), 2.5, 0.5, facecolor='g')

fig4 = plt.figure(figsize=(7, 4))
ax4 = fig4.add_subplot()

ax4.add_line(cos2)
ax4.add_patch(rect)
ax4.set(xlim=(-2*np.pi, 2*np.pi), ylim=(-1, 1))

plt.show()