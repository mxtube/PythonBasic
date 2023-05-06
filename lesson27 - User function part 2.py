"""
Lesson 27 - User function. Part 2
05.05.2023 @ Kirill Kuznetsov
"""

# Example 1
# def get_sum(c=0, d=1, a, b): - No good
def get_sum(a, b, c=0, d=1):
    return a + b + c + d


print(get_sum(1, 2, 5, 7))
print(get_sum(1, 2, 5))
print(get_sum(1, 2, d=5))
print(get_sum(1, 2))

# print(sep='', 'hello') - No good

# Example 2
# *arg - position (tuples)
# **kwarg - dictionary


def get_addition(*args):
    print(args)
    print(sum(args))
    return sum(args)


print(get_addition(5, 3, 5))


def func(**kwargs):
    print(kwargs)


func(a=1, b=5, c=20)
func(a=1, b=5.0, c='example')


def f(a, k, *args, **kwargs):
    print(a, k, args, kwargs)


f(1, 2, 3, 4.0, b=5, c='re')