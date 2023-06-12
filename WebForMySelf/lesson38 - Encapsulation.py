"""
Lesson 38 - Encapsulation
10.05.2023 @ Kirill Kuznetsov
"""

from classes37 import Person

person1 = Person(name='Katy')
person1.print_info()

person2 = Person('Maxim')
# person2.name = 'Mary'  # No good
# person2.__age = 30  # No good
# print(person2.__age)  # Err
# print(person2._Person__age)  # Access method (magic) to encapsulation
# print(person2.get_age())
# person2.set_age('1')  # Wrong age
# person2.set_age(-1)  # Wrong age
# person2.set_age(122)  # Wrong age
# person2.set_age(25)
print(person2.age)
person2.age = 35
person2.print_info()
