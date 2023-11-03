"""
Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару,
которую необходимо посчитать.  Вводится список чисел.
Все числа списка находятся на разных строках
"""

from my_Library import create_list_numbers as create

my_list = create(15)
print(my_list)

count = 0
pairs_list = []
for item in set(my_list):
    pairs = my_list.count(item)//2
    count += pairs
    if pairs:
        [pairs_list.append(item) for _ in range(pairs*2)]
    [my_list.remove(item) for  _ in range(pairs*2)]

print(pairs_list)
print(my_list)
print(f"у нас {count} пар элементов.")


#               first way
# check_dic = {item: my_list.count(item)//2
#              for item in my_list if my_list.count(item) > 1}
# print(check_dic)
# print(f"sum double: {sum(check_dic.values())}")
