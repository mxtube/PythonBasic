"""
Lesson 40 - Inheritance
10.05.2023 @ Kirill Kuznetsov
"""

from classes40 import Person, Employee

person = Person('Katy', 33)
# person.age = 35
person.print_info()

employee = Employee('Harry', 30)
employee.print_info()
