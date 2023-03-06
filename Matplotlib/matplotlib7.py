import numpy as np
import matplotlib.pyplot as plt

# 1 сетка появится сформируется в текущих координатных осях
y = np.arange(0, 5, 1)
x = np.array([a * a for a in y])
y2 = [0, 2, 3, 4, 5, 7]
x2 = [i + 1 for i in y2]
lines = plt.plot(x, y, x2, y2)
plt.grid()
plt.show()

# 2 Помимо обычной крупной сетки (major grid) можно наложить более мелкую (minor grid) минорную сетку
y3 = np.arange(0, 5, 1)
x3 = np.array([a*a for a in y])
y4 = [0, 2, 3, 4, 5, 7]
x4 = [i+1 for i in y2]
lines2 = plt.plot(x, y, x2, y2)
plt.minorticks_on()       # включить режим отображения минорной сетки
plt.grid(which='major', color = '#444', linewidth = 1) # в функции grid() прописать два типа сеток (мажорную и минорную)
plt.grid(which='minor', color='#aaa', ls=':')
plt.show()

# Создание надписей и подписей
'''
У каждой оси (объекта Axes) можно определять следующие текстовые элементы:

title – заголовок для осей;
xlabel, ylabel – подписи для каждой из осей;
text – произвольная текстовая информация в области осей;
annotate – аннотация (текст с указателем).
Также, у окна в целом можно задавать такие текстовые элементы:

subtitle – заголовок для фигуры (окна);
figtext – размещение произвольной текстовой информации в области окна.
'''
# 3
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
plt.figtext(0.05, 0.6, 'Текст в области окна', fontsize=24, color='r')
fig.suptitle('Заголовок окна')
ax.set_xlabel('Ox')
ax.set_ylabel('Oy')

ax.text(0.05, 0.1, 'Произвольный текст в координатных осях')
ax.annotate('Аннотация', xy=(0.2, 0.4), xytext=(0.6, 0.7),
            arrowprops={'facecolor': 'gray', 'shrink': 0.1})

plt.show()

