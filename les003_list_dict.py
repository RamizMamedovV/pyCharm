"""
Задаем список из случайных чисел. Нужно составить новый список
из неповторяющихся чисел
"""

from random import randint as rnd

my_list = [rnd(0, 10) for _ in range(10)]
print(my_list)

res_list = []

for i in my_list:
    if my_list.count(i) == 1:
        res_list.append(i)
print(res_list)


#                                   third method
# dic = {}
# for item in my_list:
#     dic[item] = dic.get(item,0) + 1
# print(dic)
#
# res_list = []
# for key, value in dic.items():
#     if value == 1:
#         res_list.append(key)
# print(res_list)


#                                   second method
# dic = {}
#
# for i in my_list:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i] += 1
#
# print(dic)
# res_list = []
# for (k, v) in dic.items():
#     if dic[k] == 1:
#         res_list.append(k)
# print(res_list)

#                               first method
# list_set = set(my_list)
# print(list_set)
#
# res_list = []
# count = 0
# for i in list_set:
#     for j in my_list:
#         if i == j:
#             count += 1
#     if count == 1:
#         res_list.append(i)
#     count = 0
# print(res_list)

dic_example = {1: "one", 2: "two", 3: "three"}
print(dic_example.get(1, "notFound"))
print(dic_example.get(7, "notFound"))
print(dic_example.get(3, "notFound"))
print(dic_example)
dic_example.setdefault(1, "five") # если есть такой ключ - не перезапишет
dic_example.setdefault(5, "five") # если нет такого ключа - запишет
print(dic_example)
