import numpy as np

# Функции sum, mean, min и max

a = np.array([ 1,  2,  3, 10, 20, 30])
print(a)

a.sum()    # 66
a.mean()  # 11.0
a.max()    # 30
a.min()    # 1

a.resize(3, 2)
a.sum()  # 66

a.sum(axis=0)  # array([24, 42])
a.sum(axis=1) # array([ 3, 13, 50])

a.max(axis=0)  # array([20, 30])
a.min(axis=1)  # array([ 1,  3, 20])
a.max(axis=1)  # [ 2 10 30]

# Базовые математические функции

# np.abs(x) - Вычисление модуля от аргумента(ов)x; xможет быть числом, списком или массивом.
# np.amax(x) - Нахождение максимального значения от аргумента(ов)x
# np.amin(x) - Нахождение минимального значения от аргумента(ов)x
# np.argmax(x) - Нахождение индекса максимального значения дляx
# np.argmin(x) - Нахождение индекса минимального значения дляx.
# np.around(x) - Округление до ближайшего целого.
# np.mean(x) - Вычисление среднего значения.
# np.log(x) - Вычисление натурального логарифма.
# np.log2(x) - Вычисление логарифма по основанию 2.
# np.log10(x) - Вычисление логарифма по основанию 10.

a = np.array([-1, 1, 5, -44, 32, 2])

np.abs(a) # array([ 1,  1,  5, 44, 32,  2])
np.abs([-1, 1, 5, -44, 32, ])# array([ 1,  1,  5, 44, 32])
np.abs(-10.5) # 10.5

# Эти примеры демонстрируют разные типы входных данных: массив, список, число.
# Все это допустимо использовать в математических функциях

np.amax(a) # 32
np.log(a) # array([nan, 0. , 1.60943791,  nan, 3.4657359,0.69314718])
np.around(0.7) # 1.0

# Функции amin, amax, mean, argmax, argmin, при работе с многомерными матрицами, могут делать вычисления по строго определенной оси

a.resize(2, 3)
np.amax(a, axis=0)  # array([-1, 32,  5])
np.argmax(a, axis=1) # array([2, 1], dtype=int32)

# Тригонометрические функции

# np.sin(x) - Вычисление синуса угла x (в радианах); xможет быть числом, списком,
                 # массивом (это правило распространяется на все функции этой таблицы)
# np.cos(x) - Вычисление косинуса угла(ов) x.
# np.tan(x) - Вычисление тангенса угла(ов) x.
# np.arccos(x) - Арккосинус угла(ов) x.
# np.arcsin(x) - Арксинус угла(ов) x.
# np.arctan(x) - Арктангенс угла(ов) x.

a = np.linspace(0, np.pi, 10)
res1 = np.sin(a) # возвращает массив синусов углов
np.sin(np.pi/3)
np.cos([0, 1.57, 3.17])
res2 = np.cos(a) # возвращает массив косинусов углов
np.arcsin(res1) # возвращает арксинусы от значений res1

# Функции генерации псевдослучайных чисел

# random.rand() - Генерация чисел с равномерным законом распределения
# np.random.randint() - Генерация целых чисел с равномерным законом распределения
# np.random.randn() - Генерация нормальных случайных значений
# np.random.seed() - Установка начального состояния генератора

# В самом простом случае, функция rand() позволяет получать случайные числа в диапазоне от 0 до 1:
np.random.rand() # вещественное случайное число от 0 до 1
np.random.rand(5) # array([0.78191696, 0.66581136, 0.46458873, 0.76416839, 0.28206656])
np.random.rand(2, 3) # массив 2x3

np.random.randint(10) # генерация целых чисел в диапазоне [0; 10)
np.random.randint(5, 10)# генерация в диапазоне [5; 10)

np.random.randint(5, size=4) # array([3, 1, 1, 4])
np.random.randint(1, 10, size=(2, 5)) # матрица 2x5

# Функции rand() и randint() генерируют числа с равномерным законом распределения.
# Если нужно получать значения с другими широко известными распределениями, то используются функции:
np.random.randn() # нормальная СВ с нулевым средним и единичной дисперсией
np.random.randn(5) # массив из пяти нормальных СВ
np.random.randn(2, 3) # матрица 2x3 из нормальных СВ
np.random.pareto(2.0, size=3) # распределение Паретто с параметром 2,0
np.random.beta(0.1, 0.3, size=(3, 3)) # бета-распределение с параметрами 0,1 и 0,3

np.random.seed(13) # начальное значение генератора случайных чисел
# все последующие запуски будут давать одну и ту же последовательность чисел
np.random.randint(10, size=10) # array([2, 0, 0, 6, 2, 4, 9, 3, 4, 2])

# Функции перемешивания элементов массива

# np.random.shuffle() и np.random.permutation() перемешивают случайным образом элементы массива

a = np.arange(10) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.random.shuffle(a) # array([8, 7, 9, 6, 3, 4, 0, 2, 1, 5])
np.random.shuffle(a) # array([7, 2, 1, 5, 8, 6, 4, 3, 9, 0])
# работает она только с первой осью axis0

a = np.arange(1, 10).reshape(3, 3)
np.random.shuffle(a) # то в массиве aбудут переставлены только строки
# array([[1, 2, 3],
#        [7, 8, 9],
# [4, 5, 6]])

# Вторая функция возвращает случайную последовательность чисел, генерируя последовательность «на лету»
np.random.permutation(10) # array([8, 2, 7, 1, 0, 5, 3, 9, 4, 6])

# Функции математической статистики

# np.median(x) - Вычисление медианы величин x
# np.var(x) - Дисперсия величин x
# np.std(x) - Среднеквадратическое отклонение величин x
# np.corrcoef(x) - Линейный коэффициент корреляции Пирсона
# np.correlate(x) - Вычисление кросс-корреляции
# np.cov(x) - Вычисление ковариационной матрицы

x = np.array([1, 4, 3, 7, 10, 8, 14, 21, 20, 23])
y = np.array([4, 1, 6, 9, 13, 11, 16, 19, 15, 22])

np.median(x) # 9.0
np.var(x) # дисперсия СВX на основе реализации x
np.std(y) # СКО СВY на основе реализации y

XY = np.vstack([x, y]) # матрица 2x10
np.corrcoef(XY)
# Результатом будет матрица 2x2:
# array([[1.        , 0.93158099],
#        [0.93158099, 1.        ]])

np.cov(XY) # ковариационная матрица размерностью 2x2
np.correlate(x, y) # array([1736])
