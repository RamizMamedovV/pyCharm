"""
Дан массив, состоящий из целых чисел. Напишите программу,
определить в данном массиве количество элементов,
у которых два соседних и, при этом,
оба этих элемента меньше данного.
Сначала вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива.
Массив состоит из целых чисел.
"""
import random

my_list = [random.randint(1, 10) for _ in range(1, 10)]
print(my_list)

count = 0
for i in range(len(my_list)):
    left = my_list[i-1]
    middle = my_list[i]
    right = my_list[(i+1)%len(my_list)]
    print((i+1)%len(my_list))
    if left < middle > right:
        count += 1

print(count)


#                   second way
# count = 0
# for i in range(-1, len(my_list)-1):
#     if my_list[i-1] < my_list[i] > my_list[i+1]:
#         print(f"my_list[i] = {my_list[i]}")
#         count += 1
#
# print(f"count = {count}")

#                   first way
# def check_neighbor(left, middle, right):
#     if left < middle > right:
#         return True
#     return False


# def check_list(list_for: list):
#     length = len(list_for)
#     count = 0
#     if length > 3:
#         left = list_for[-1]
#         middle = list_for[0]
#         right = list_for[1]
#         if check_neighbor(left, middle, right):
#             count += 1
#         left = list_for[-2]
#         middle = list_for[-1]
#         right = list_for[0]
#         if check_neighbor(left, middle, right):
#             count += 1
#         for i in range(1, len(list_for) - 1):
#             left = list_for[i - 1]
#             middle = list_for[i]
#             right = list_for[i + 1]
#             if check_neighbor(left, middle, right):
#                 count += 1
#     return count
#
#
# print(check_list(my_list))
