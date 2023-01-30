import numpy as np

a = np.array([1, 2, 3, 10, 20, 30])

indx = a > 5
print(a[indx])

b = np.array([1, 2, 3, 4, 5, 6])

print(a == b)    # array([ True,  True,  True, False, False, False])
print(a >= b)    # array([ True,  True,  True,  True,  True,  True])
print(a <= b)    # array([ True,  True,  True, False, False, False])
print(a != b)    # array([False, False, False,  True,  True,  True])

# Функции greater, less, equal

# Вместо записи операторов в NumPy имеются функции сравнения: greater(), less() и equal()

# greater(a, b) – выполняет сравнение a > b;
# less(a, b) – выполняет сравнение a < b;
# equal(a, b) – выполняет сравнение a == b.

print(np.greater(a, b)) # array([False, False,  True, False])
print(np.less(a, b)) # array([ True,  True, False, False])
print(np.equal(a, b)) # array([False, False, False,  True])

# Функции array_equal, all и any

# сравнениe массивов - необходимо получать только одно значение True или False, а не объект array
if np.array_equal(a ,b):    # специальная функция np.array_equal()
     print("a == b")

# хотя бы один элемент массива удовлетворяет указанному условию, то можно воспользоваться функцией any()
# для массива a = array([ 1,  2,  3, 10, 20, 30])
np.any(a > 5)    # True
np.any(a == 5)    # False
np.any(a == b)    # True

# все ли элемента массива удовлетворяют условию, то используется функция all()
np.all(a > 5)       # False
np.all(a > 0)       # True
np.all(a == b)     # False


# Значения -inf, inf и nan

# разделим все значения массива a на 0, все элементы примут значение inf
# infinity – бесконечность. Действительно, при делении на 0 получаем бесконечность.
#  inf – это полноценный элемент массивов

b = np.array([1, 2, np.inf])
print(b*0) # array([ 0.,  0., nan]) nan - not a number (не число)
# значение nan указывает, что в результате арифметической операции третий элемент перестал быть каким-либо числовым значением
# любые арифметические операции с nan приводят к nan


# Функции isnan и isinf

# Так как элементы inf и nan не относятся к числам, то для их идентификации, проверки, что текущий элемент массива
# принимает одно из этих значений, существуют функции isnan() и isinf(). Они возвращают True, если элемент
# равен nan и inf и Flase – в противном случае

b = np.array([1, 2, np.nan, np.inf, -np.inf])

np.isinf(b)  # array([False, False, False,  True,  True])
np.isnan(b)  # array([False, False,  True, False, False])

# На выходе имеем массив с булевыми значениями и True стоит на местах inf (при вызове isinf) и nan (при вызове isnan).
# Далее, используя этот массив можно исключить нечисловые элементы из массива
indx = np.isinf(b)
print(b[~indx])  # array([ 1.,  2., nan])
# Здесь исключаются все элементы inf, а операция ~indx инвертирует булевы значения. Аналогично можно отфильтровать значения nan


# Дополнительные функции: isfinite, iscomplex, isreal

# при работе с массивами требуется определить: являются ли его элементы конечными числами. Для этого используется еще
# одна функция – isfinit()

# для массива b = np.array([1, 2, np.nan, np.inf, -np.inf])
np.isfinite(b) # array([ True,  True, False, False, False])

# мы можем уточнять тип числа: комплексное или действительное, с помощью функций iscompex() и isreal()
a = np.array([1+2j, 3-4j, 5])  # array([1.+2.j, 3.-4.j, 5.+0.j])
np.iscomplex(a) # array([ True,  True, False])
# последний элемент функция iscomplex() пометила как False, так как мнимая часть равна нулю

# Аналогично работает функция isreal():
np.isreal(a) # array([False, False,  True])

np.isreal(b) # array([ True,  True,  True,  True,  True])
# получим все значения True. То есть, специальные значения nan и inf отмечаются как действительные.


# Функции logical_and, logical_or, logical_not и logical_xor

# можно выполнять стандартные булевы операции И, ИЛИ, НЕ, исключающее ИЛИ, применительно к данным массивов
X = np.array([True, False, True, False])
Y = np.array([True, True, False, False])

np.logical_and(X, Y) # логическое И: array([ True, False, False, False])
np.logical_or(X, Y) # логическое ИЛИ: array([False,  True, False,  True])
np.logical_not(X) # логическое НЕ: array([False,  True, False,  True])
np.logical_xor(X, Y) # XOR: array([ True,  True,  True,  True])

# Все те же операции можно проводить и с числовыми значениями, полагая, что 0 – это False, а любое другое число – True
a = np.array([1, 0, 2, 0])
b = np.array([3, 4, 0, 0])
np.logical_and(a, b) # array([ True, False, False, False])

