"""
Lesson 11 - String formatting
02.05.2023 @ Kirill Kuznetsov
"""

name = 'Kirill'
age = 29

# Example 1 - Basic
print('My name is ' + name + '. I\'m ' + str(age))  # No good
print('My name is %(name)s. I\'m %(age)d' % {'name': name, 'age': age})
print('My name is %s. I\'m %d' % (name, age))
print('My name is %s. I\'m %d' % ('Ivan', age))

print('Title: %s, Price: %f' % ('Apple', 150))
print('Title: %s, Price: %.2f' % ('Apple', 150))

# Example 2 - Format
print('My name is {}. I\'m {}'.format(name, age))
print('My name is {0}. I\'m {1}'.format(name, age))
print('{0}: My name is {0}. I\'m {1}'.format(name, age))
print('My name is {x}. I\'m {y}'.format(x=name, y=age))
print('My name is {x}. I\'m {y}'.format(x='Alex', y=age))

# Example 3 - f-strings (python>3.6)
print(f'My name is {name}. I\'m {age}')
print(f'My name is {name}. I\'m {age + 5}')

print('5 + 2 = {}'.format(5 + 2)) # No good
print(f'5 + 2 = {5 + 2}')