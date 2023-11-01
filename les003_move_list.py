"""
Дана последовательность из N чисел и число K.
Необходимо сдвинуть всю последовательность (сдвиг - циклический)
 на K элементов вправо, K - положительное число.
"""
from random import randint as rnd

list_first = [rnd(0, 10) for _ in range(10)]
print(list_first)

k = int(input("Enter K: "))

#                   first way
# new_list = []
# for i in range(len(list_first)):
#     new_list.append(list_first[(i+k)%len(list_first)])
# print(new_list)

#                   next way
for i in range(k):
    list_first.insert(0, list_first.pop())
print(list_first)
print(list_first.pop(2))    # работает с индексом!!!!! возвращает по индексу,
                            # затем его удалит сборзик мусора!!!
print(list_first)
print(list_first.remove(5)) # работает со значением!!! если есть такое значение
                            # то, оно удалится
print(list_first)

#                   next way
# if k <= len(list_first) - 1:
#     list_new = [*list_first[k:], *list_first[:k]]
#     print(list_new)
# else:
#     print("K is not correct")