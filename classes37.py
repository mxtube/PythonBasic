"""
Lesson 37 - Classes
10.05.2023 @ Kirill Kuznetsov
"""


class Person:

    # name = 'Kirill'

    def __init__(self, name):
        self.name = name
        self.__age = 20

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.__age}')

    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, value):
    #     if value in range(1, 101):
    #         self.__age = value
    #     else:
    #         print('Wrong age')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value in range(1, 101):
            self.__age = value
        else:
            print('Wrong age')
