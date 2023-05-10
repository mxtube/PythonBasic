"""
Lesson 37 - Classes
10.05.2023 @ Kirill Kuznetsov
"""


class Person:

    # name = 'Kirill'

    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f'Hello, my name is {self.name}')