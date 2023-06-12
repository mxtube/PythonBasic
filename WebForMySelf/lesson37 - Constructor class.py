"""
Lesson 37 - Constructor class
10.05.2023 @ Kirill Kuznetsov
"""

# import classes37
from classes37 import Person

person1 = Person(name='Katy')
person1.print_info()

person2 = Person('Maxim')
# person2.name = 'Mary'  # No good
person2.print_info()
