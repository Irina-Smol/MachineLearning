import numpy as np

print(np.__version__)

my_list = [4, 8, 15, 16, 23, 42]
me_array_from_list = np.array(my_list)
print(me_array_from_list)
print(me_array_from_list * 10)

my_tuple = (14, -3.57, 5 + 7j)
print(np.array(my_tuple))
print(my_tuple * 5)

print('---------------')

print(np.arange(10))
print(len(np.arange(10, 21)))
np.arange(10, 21, 2)

print('---------------')

# Задача: разместить стулья (11 штук) для 30 человек
np.linspace(0, 30, 11) # спользуется для генерации последовательности чисел в линейном пространстве с одинаковым размером шага
# одинаковое расстояние между стульями

# посчитать кол-во элементов в массиве
print(np.linspace(0, 30, 11).size)
my_line = np.linspace(0, 30, 11, retstep=True) # вернет интервал с которым расставлены числа

print('---------------')

# zeros() для заполнения пустыми значениями (нулями), ones() для заполнения единицами

ave_vector = np.array([4, 8, 15, 16, 23, 42])
print(ave_vector[1])
print(ave_vector[-2])
ave_vector[1] = 14
print(ave_vector)

print('---------------')

ave_array = np.arange(35)
ave_array.shape = (7, 5)
print(ave_array)
print(ave_array[1]) # [ 5  6  7  8  9]
print(ave_array[5, 2]) # 27

print('---------------')

av_array = np.array([4, 8, 15, 16, 23, 42])
zero_mod_2_mask = 0 == (av_array % 2)
print(zero_mod_2_mask)
sub_array = av_array[zero_mod_2_mask]
print(sub_array)
print(sub_array[sub_array > 10])
zero_mod_4_mask = 0 == (av_array % 4)
combined = np.logical_and(zero_mod_2_mask, zero_mod_4_mask)
print(combined)

print('---------------')

ave_3D_array = np.arange(70)
ave_3D_array.shape = (2, 7, 5)
print(ave_3D_array)
print(5 * ave_3D_array - 10)

left_matrix = np.arange(6).reshape((2, 3))
right_matrix = np.arange(15).reshape((3, 5))
# reshape - делает копию массива и изменяет его форму, не изменяя оригинальный массив

print(np.dot(left_matrix, right_matrix)) # перемножение матриц

print('---------------')

ave_2D_array = np.ones(35, dtype='int_').reshape((7, 5)) * 5
print(ave_2D_array)

print('---------------')

ave_random = np.random.random((7, 5))
np.set_printoptions(precision=4) # точность до 4 знаков после запятой
print(ave_random)

print('---------------')

employee_data = [('name', 'S6'), ('height', 'f8'), ('weight', 'f8')]
print(employee_data)

employees = np.zeros((3), dtype=employee_data)
print(employees)

employees[2] = ('Dan', 200, 100)
print(employees)

print('---------------')

trial_array = (np.arange(24)).reshape((2, 3, 4))
trial_array2 = np.append(trial_array, [5, 6, 7, 8])
print(trial_array)
print(trial_array2)