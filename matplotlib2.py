import matplotlib.pyplot as plt
import numpy as np

plt.plot([1, 2, -6, 0, 4]) #1
plt.show()

y = np.array([1, 2, -6, 0, 4]) # 2
plt.plot(y)
plt.show()

# 3
x = np.array([4, 5, 6, 7, 8]) # значения по абциссе
y = np.array([1, 2, -6, 0, 4]) # значения по оси ординат
plt.plot(x, y)
plt.show()

# функция plot() при отображении этих данных соединяет прямыми линиями точки с указанными координатами
# 4
x = np.array([1, 1, 5, 5, 1])
y = np.array([1, 5, 5, 1, 1])
plt.plot(x, y)
plt.show()

# рисовать графики с разными шагами по оси абсцисс (5)
y = np.arange(0, 5, 1)             # [0, 1, 2, 3, 4]
x = np.array([a*a for a in y])   # [ 0,  1,  4,  9, 16]
plt.plot(x, y)
plt.grid() # наложить сетку
plt.show()

# в этих же осях отобразить еще один график (6), оба графика отображаются совершенно независимо
y = np.arange(0, 5, 1)
x = np.array([a*a for a in y])
y2 = [0, 1, 2, 3]
x2 = [i+1 for i in y2]
plt.plot(x, y, x2, y2) # или plt.plot(x, y)
                           # plt.plot(x2, y2)
plt.grid()
plt.show()

'''
Изменение стилей линий у графиков

Если третьим параметром в plot() указать строку с двумя дефисами:
plt.plot(x, y, '--')
то график будет изображен не сплошной линией, а штрихами

'-' - Непрерывная линия (используется по умолчанию)
'--' - Штриховая линия
'-.' - Штрихпунктирная линия
':' - Пунктирная линия
'None' или ' ' - Без рисования линии
'''
# 7
y = np.arange(0, 5, 1)
x = np.array([a*a for a in y])
y2 = [0, 1, 2, 3]
x2 = [i+1 for i in y2]
plt.plot(x, y, '--')
plt.plot(x2, y2, ':')
plt.show()
lines = plt.plot(x, y, '--')
print(lines) # Функция plot возвращает список на объекты Line2D, в консоли список из одного объекта(функция отображает один график)
plt.setp(lines, linestyle='-.') # Через этот объект можно непосредственно управлять графиком, поменять тип линии
plt.show() # 8
lines = plt.plot(x, y, '--', x2, y2, ':')  # коллекция lines будет содержать два объекта Line2D
plt.setp(lines, linestyle='-.') # оба будут отображены штрихпунктирной линией
plt.show() # 9

# Изменение цвета линий графиков
# <p align=center>{'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'} Цвет можно понять по английскому названию указанной первой буквы

lines = plt.plot(x, y, '--g', x2, y2, ':m')
plt.show() # 10
lines = plt.plot(x, y, '--g', x2, y2, ':m', color='r')
plt.show() # 11

'''
Преимущество этого параметра в возможности указания цвета не только предопределенными символами, 
но, например, в шестнадцатиричной записи:

lines = plt.plot(x, y, '--g', x2, y2, ':m', color='#0000CC')
Или в виде кортежей формата:
         RGB и RGBA
lines = plt.plot(x, y, '--g', x2, y2, ':m', color=(0, 0, 0))
lines = plt.plot(x, y, '--g', x2, y2, ':m', c=(0, 0, 0, 0.5))
'''

# Изменение маркеров точек у графиков

plt.plot(x2, y2, ':o')
plt.show() # 12

lines = plt.plot(x, y, '-go', x2, y2, 's:m')
plt.show() # 13

lines = plt.plot(x, y, '-go', x2, y2, 's:m', marker='d')
lines = plt.plot(x, y, '-go', x2, y2, 's:m', marker='d', markerfacecolor='w')
plt.show() # 14


# Именованные параметры функций setp() и plot()
plt.setp(lines[0], linestyle='-.', marker='s', markerfacecolor='b', linewidth=4)
# отображение графика штрихпунктирной линией, квадратным маркером с синей заливкой и толщиной линии, равной 4 пикселя

'''
alpha - Степень прозрачности графика (значение от 0 до 1)
color или c - Цвет линии
dash_capstyle - Стиль штриховых конечных точек ['butt' | 'round' | 'projecting']
dash_joinstyle - Стиль штриховых соединительных точек ['miter' | 'round' | 'bevel']
data - Данные графика в формате (x, y), где x, y – массивы numpy
linestyle или ls - Стиль линии [ '-' | '--' | '-.' | ':' | 'steps' | ...]
linewidth или lw - Толщина линии (вещественное число)
marker - Маркер точек
markeredgecolor или mec - Цвет границ маркеров
markeredgewidth или mew - Толщина границы маркеров (вещественное число)
markerfacecolor или mfc - Цвет заливки маркеров
markersize или ms - Размер маркеров
solid_capstyle - Стиль конечных точек непрерывной линии ['butt' | 'round' | 'projecting']
solid_joinstyle - Стиль соединительных точек непрерывной линии ['miter' | 'round' | 'bevel']
visible - Показать/скрыть график [True | False]
xdata - Значения для оси абсцисс (массив numpy)
ydata - Значения для оси ординат (массив numpy)
'''

# Заливка областей графика

# fill_between(x,  y1,  y2=0,  where=None,  interpolate=False,  step=None,  *, data=None, **kwargs)
# Основные параметры здесь следующие:
# x, y1 – массивы значений координат x и функции y1;
# y2 – массив (или число) для второй кривой, до которой производится заливка;
# where – массив булевых элементов, который определяет области для заливки.

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x)
plt.plot(x, y)
plt.fill_between(x, y)
plt.show() # 15
plt.fill_between(x, y, 0.5)
plt.show() # 16
plt.fill_between(x, y, 0.5, where=(y < 0))
plt.show() # 17
plt.fill_between(x, y, where=(y < 0), color='r', alpha=0.5)
plt.fill_between(x, y, where=(y > 0), color='g', alpha=0.5)
plt.show() # 18