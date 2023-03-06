import numpy as np
import matplotlib.pyplot as plt

# 1
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(0, 5, 0.25))
ax.plot(np.arange(0, 10, 0.5))
plt.show()

# 2 отобразить легенду – их краткое описание, с помощью метода: ax.legend()
fig2 = plt.figure(figsize=(7, 4))
ax2 = fig2.add_subplot()
ax2.plot(np.arange(0, 5, 0.25), label='line1')
ax2.plot(np.arange(0, 10, 0.5), label='line2')
ax2.legend()
plt.show()

# 3
fig3 = plt.figure(figsize=(7, 4))
ax3 = fig3.add_subplot()
ax3.plot(np.arange(0, 5, 0.25), '--o', label='line1')
ax3.plot(np.arange(0, 10, 0.5), ':s', label='line2')
ax3.legend()
plt.show()

# 4
fig4 = plt.figure(figsize=(7, 4))
ax4 = fig4.add_subplot()
line1, = ax4.plot(np.arange(0, 5, 0.25), '--o', label='line1')
line2, = ax4.plot(np.arange(0, 10, 0.5), ':s', label='line2')
ax4.legend((line2, line1), ['Линия 2', 'Линия 1'])
plt.show()

# 5
fig5 = plt.figure(figsize=(7, 4))
ax5 = fig5.add_subplot()
line3, = ax5.plot(np.arange(0, 5, 0.25), '--o', label='line1')
line4, = ax5.plot(np.arange(0, 10, 0.5), ':s', label='line2')
ax5.legend((line4, line3), ['Линия 2', 'Линия 1'], loc='upper right')
plt.show()

# 6
fig6 = plt.figure(figsize=(7, 4))
ax6 = fig6.add_subplot()
line5, = ax6.plot(np.arange(0, 5, 0.25), '--o', label='line1')
line6, = ax6.plot(np.arange(0, 10, 0.5), ':s', label='line2')
ax6.legend((line6, line5), ['Линия 2', 'Линия 1'], bbox_to_anchor=(0.5, 0.7))
plt.show()

# 7
fig7 = plt.figure(figsize=(7, 4))
ax7 = fig7.add_subplot()
line7, = ax7.plot(np.arange(0, 5, 0.25), '--o', label='line1')
line8, = ax7.plot(np.arange(0, 10, 0.5), ':s', label='line2')
ax7.legend((line8, line7), [r'$f(x) = a \cdot b + c$', r'$f(x) = k \cdot x + b$'])
plt.show()


