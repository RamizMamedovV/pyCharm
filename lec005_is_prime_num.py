"""
Проверка числа, является ли оно простым?
"""
import math


def check_number(num: int):
    if num in (0, 4, 6, 8):
        print("This number is not prime")
    elif num in (1, 2, 3, 5, 7):
        print("This number is prime")
    else:
        sqrt_num = int(math.sqrt(num)) + 1
        for i in range(2, sqrt_num):
            if not num % i:
                print("This number is not prime")
                return
        print("This number is prime")


number = int(input("Enter your number: "))
check_number(number)