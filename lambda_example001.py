my_list = [1, 2, 3, 5, 8, 15, 23, 38]


def foo(a):
    return a ** 3


def math(op, a):
    #print(op(a))
    return [op(i) for i in a if i % 2 == 0]


y = math((lambda z: z ** 2), my_list)


# math(lambda x: x ** 2, 5)
# math(lambda x: x ** 3, 5)
print(y)

