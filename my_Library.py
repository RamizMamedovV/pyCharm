from random import randint as rnd


def create_list_numbers(length=10, start=0, end=10):
    return [rnd(start, end) for _ in range(length)]