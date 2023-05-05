"""
Lesson 13 - Cycle For and While
02.05.2023 @ Kirill Kuznetsov
"""

# Example 1 - Endless cycle
while True:
    print('Hello Python!')
    break

i = 1
while i <= 10:
    print(i, end=' ')
    # i = i + 1
    i += 1

# Example 2 - For cycle
s = 'Hello Python'
for l in s:
    if l == ' ':
        continue;
    print(f'"{l}"', end=' ')

# Example 3 - Operator break
for i in 'Hello Python':
    if i == ' ':
        break
    print(i, end=' ')

# Example 4 - Operator else
for i in 'Hello Python':

    print(i, end=' ')
else:
    print('\nNo spaces')

# Homework
# Create a list by year from 1900 to 2023
# Answer 1
for year in range(1900, 2023):
    print(year)

# Answer 2
year = 1900
while year <= 2023:
    print(year)
    year += 1
else:
    print('Done')
