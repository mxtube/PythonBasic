"""
Lesson 28 - User function. Part 3
06.05.2023 @ Kirill Kuznetsov
"""


def func(name, *args):
    """
    Return message with name and age.

    :param name: Firstname
    :type name: str

    :param args: Age
    :type name: int
    :return: Return type str
    """
    return f'Hello {name}, im old {args[0]}'


print(func('Kirill', 19))


a = 5  # global


def f():
    a = 10  # local
    a += 1
    print(a)


f()
print(a)


# Example 3 - Global
x = 66


def a():
    global x
    x += 1
    print(x)


print(x)
a()
print(x)

l1 = [33, '44', 55]


def o(li):
    return [i * 2 for i in li]


print(o(l1))


def o2(li):

    def get_mult(num):
        return int(num) * 2

    return [get_mult(i) for i in li]


print(o2(l1))


def o3(li):

    def get_mult(num):
        if isinstance(num, int):
            return num * 2

    return [get_mult(i) for i in li]


print(o3(l1))


def o4(li):

    def get_mult(num):
        if isinstance(num, int):
            return num * 2

    return [get_mult(i) for i in li if get_mult(i)]


print(o4(l1))


def o5(li):

    def get_mult(num):
        return num * 2

    return list(map(get_mult, li))


print(o5(l1))
