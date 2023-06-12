"""
Lesson 40 - Class Person
10.05.2023 @ Kirill Kuznetsov
"""


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.age}')

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, value):
        if value in range(1, 101):
            self.age = value
        else:
            print('Wrong age')


class Employee(Person):
    pass
