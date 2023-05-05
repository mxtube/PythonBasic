"""
Lesson 26 - User function
05.05.2023 @ Kirill Kuznetsov
"""

def hello_python(name, word):
    print('Hello, ' + name + '. Say ' + word)


hello_python('John', 'hi')
hello_python('Katy', 'hello')


def addition(a, b):
    print(f'{a} + {b} = {a + b}')


x = 2
y = 5

addition(1, 3)
addition(x, y)


def get_addition(a, b):
    return a + b


print(get_addition(3, 3))


def hello():
    print('Hi')


print(hello())  # return None
