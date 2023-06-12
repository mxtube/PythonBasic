"""
Lesson 14 - Lists
02.05.2023 @ Kirill Kuznetsov
"""

# Example 1

print(l1)

# Example 2
l2 = list('hello')
print(l1, l2, sep='\n')

# Example 3
l3 = list((1, 2, 3))
print(l3)

# Example 4
l4 = [i for i in 'hello']
print(l4)

# Example 5
l5 = [i for i in 'hello python' if i != ' ']
print(l5)

# Example 6
l6 = [i for i in 'hello python' if i not in ['a', 'e', 'i', 'o', 'u', ' ', 'y']]
print(l6)

# Example 7
l7 = [i * 3 for i in 'hello python' if i not in ['a', 'e', 'i', 'o', 'u', ' ', 'y']]
print(l7)

# Example 8
print(range(10))  # generator
print(list(range(20, 90)))
print(list(range(20, 90, 2)))

# Example 9 - For in For
for i in range(1, 5):
    print(f'External loop #{i}')
    for j in range(1, 3):
        print(f'\tLocal loop #{j}')

# Homework
# Create multiplication table
# Answer 1
print('Multiplication table')
for i in range(1, 11):
    for j in range(1, 11):
        print(f'\t{i} * {j}')

# Answer 2
for i in range(1, 10):
    for k in range(2, 10):
        print(f'{i} * {k} = {i * k}\t', end='')
    print('')
else:
    print('Well done')
