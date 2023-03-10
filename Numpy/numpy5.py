#Транспонирование матриц и векторов

import numpy as np

a = np.array([(1, 2, 3), (1, 4, 9), (1, 8, 27)])
b = a.T
b[0, 1] = 10

# имеется одномерный массив
x = np.arange(1, 10)
y = x.T
"""
массив x имеет только одну размерность, поэтому здесь нет понятия строк и столбцов. Соответственно, 
операция транспонирования ни к чему не приводит. Чтобы получить ожидаемый эффект, нужно добавить к 
массиву еще одну ось
"""
x.shape = 1, -1
y = x.T # вектор-столбец 9x1

# Добавление и удаление осей
#np.expand_dims(a, axis) – добавление новой оси;
#np.squeeze(a[, axis]) – удаление оси (без удаления элементов).

x_test = np.arange(32).reshape(8, 2, 2) # массив 8x2x2
x_test4 = np.expand_dims(x_test, axis=0)
s = x_test4.shape # (1, 8, 2, 2)
a = np.append(x_test4, x_test4, axis=0) # размерность (2, 8, 2, 2)

b = np.delete(a, 0, axis=0) # размерность (1, 8, 2, 2)
b = np.expand_dims(x_test4, axis=-1) # размерность (1, 8, 2, 2, 1) добавить последнюю ось
c = np.squeeze(b) # размерность (8, 2, 2) удалить все оси с одним элементом

c = np.squeeze(b, axis=0) # удалит только ось axis0, не затронув другие
c = np.squeeze(b, axis=1) # ошибка, на оси axis1 8 элементов

# Объект newaxis
a = np.arange(1, 10) # array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a[np.newaxis, :] # добавление оси axis0
b.shape # (1, 9)

c = a[np.newaxis, :, np.newaxis]
c.shape # (1, 9, 1)
