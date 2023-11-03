"""
Напишите программу, которая принимает на вход строку,
и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью
постфикса формата _n.
"""
from random import randint as rnd

my_list = [rnd(1, 10) for _ in range(10)]
print(my_list)
my_dic = {}

for i in my_list:
    my_dic[i] = my_dic.get(i, 0) + 1

    print(i if my_dic[i] == 1 else f"{i}_{my_dic[i] - 1}", end=", ")
    # if my_dic[i] == 1:
    #     print(i, end=', ')
    # else:
    #     print(f"{i}_{my_dic[i] - 1}", end=", ")


#                   first way
# set_list = set(my_list)
# count = 0
# for i in set_list:
#     for j in range(len(my_list)):
#         if i == my_list[j]:
#             count += 1
#             if count > 1:
#                 num = count - 1
#                 my_list[j] = f"{my_list[j]}_{num}"
#     count = 0
# print(my_list)