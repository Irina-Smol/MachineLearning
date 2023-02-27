'''
Положение меток на координатных осях

Пакет matplotlib по умолчанию довольно хорошо расставляет метки сетки при отображении графиков.
Но если требуется их изменить, то мы легко можем это делать с помощью двух специальных методов:
set_major_locator() – управление рисками крупной сетки;
set_minor_locator() – управление рисками мелкой сетки.
качестве аргумента они принимают экземпляр класса, унаследованный от базового класса:
matplotlib.ticker.Locator
'''

# NullLocator
# используется для сокрытия меток по выбранной оси

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.25))

lc = NullLocator()
ax.grid() # включаем сетку
#ax.xaxis.set_major_locator(lc) # отключаем риски у оси Ox сокрытие вертикальных линий (сокрытие меток по оси ОХ)
#ax.yaxis.set_major_locator(lc) - сокрытие горизонтальных линий (сокрытие меток по оси ОУ)
plt.show()


# LinearLocator
# используется для задания нужного числа меток по выбранной оси графика

ax.grid()
# ax.yaxis.set_major_locator(LinearLocator(5)) - # взять 5 меток
plt.show()



