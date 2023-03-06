import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 4), facecolor='#eee')
fig.set(facecolor='#eee')
ax = fig.add_subplot()
ax.set(facecolor='#AAFFAA')
plt.figtext(0.05, 0.6, 'Текст в области окна', fontsize=24, color='r')
fig.suptitle('Заголовок окна')
plt.xlabel('Ox')
plt.ylabel('Oy')

ax.text(15, 2, 'Текст', bbox={'boxstyle':'darrow', 'facecolor': '#AAAAFF'})
ax.annotate('Аннотация', xy=(0.2, 0.4), xytext=(0.6, 0.7),
            arrowprops={'facecolor': 'gray', 'shrink': 0.1})
ax.plot(np.arange(0, 5, 0.25))
plt.show()
