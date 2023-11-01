"""
Задача 10: На столе лежат "n" монеток.
Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
"""
from random import randint as rnd

n = int(input("enter amount of coins: "))
num = 0
countNull = 0
countOne = 0

for i in range(n):
    num = rnd(0, 1)
    print(num, end=', ')
    if num == 0:
        countNull += 1
    else:
        countOne += 1
print('\n', f'"1" {countOne} pcs' if countNull > countOne else f' "0" {countNull} pcs')
