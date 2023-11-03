"""
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом массиве),
которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве,
затем N чисел - элементы массива.
Затем число M - количество элементов во втором массиве.
Затем элементы второго массива
"""
from random import randint as rnd

list_first = [rnd(1, 20) for _ in range(10)]
list_second = [rnd(1, 20) for _ in range(10)]

print(list_first)
print(list_second)

#           List Comprehension
result = [j for j in list_first if j not in list_second]
print(result)
