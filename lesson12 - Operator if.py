"""
Lesson 12 - Operator If
02.05.2023 @ Kirill Kuznetsov
"""

# Example 1 - Basic
print(2 > 3)  # False
print(2 < 3)  # True
print(2 >= 2)  # True

# Example 2 - If statement
'''
if condition 1:
    code block 1
elif condition 2:
    code block 2
else:
    code block 3
'''
x = 0
if x:
    print('Variable x return TRUE')
else:
    print('Variable x return FALSE')

# Example 3
if -3:
    print('Variable x return TRUE')
else:
    print('Variable x return FALSE')

# Example 4
light = '0x3112'
if light == 'red':
    print('Stop')
elif light == 'yellow':
    print('Wait')
elif light == 'green':
    print('Go')
else:
    print('Error semafore')

# Example 5
age = int(input('How old are you?'))

if age >= 18:
    print('Welcome')
else:
    print('It\'s too early for you')
    print(f'You are missing another {18 - age} years')

# Example 6 - Bool operator OR
time = 12

if time < 12 or time > 13:
    print('Shop is open')
else:
    print('Shop is close')

# Example 7 - Bool operator AND
time = 11
day = 'st'

if time >= 8 and day != 'su':
    print('Shop is open')
else:
    print('Shop is close')

# Example 8 - Condition 'not'

x = 1
if not x:
    print('Ok')
else:
    print('No')

# Example 9
x = 0

res = 'Ok' if x else 'No'
print(res)
print('Ok' if x else 'No, is false')