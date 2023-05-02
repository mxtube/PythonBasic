"""
Lesson 16 - List Methods
02.05.2023 @ Kirill Kuznetsov
"""

# Example 1
l1 = [1, 2, 3, 'hello', ['test', 10], 'world', True]
print(f'Length list: {len(l1)}')

names = ['Ivanov', 'Petrov', 'Sidorov']
print(names[1])
print(l1[3])
print(l1[4])
print('\t->', l1[4][0])

print(l1[0:3])
print(l1)

# Example 2 - Single update value
l1[2] = 'Alex'
print(l1)

# Example 3 - Range update value
l1[2:4] = [10, 15]
print(l1)

# Example 4 - Append
l1.append('Germany')
print(l1)

# Example 5 - Extend
l1.extend(names)
print(l1)

# Example 6 - Insert
l1.insert(3, 2)
print(l1)

# Example 7 - Remove (Delete first element in list), or not find call ValueError
l1.remove(10)
print(l1)

# Example 8 - Pop
''' Else not send value, remove last element '''
el = l1.pop()
print(l1, el)

# Example 9 - Count
print(l1.count(2))

# Example 10 - Sort (only one type)
# print(l1.sort())
l2 = ['hello', 'python', 'my', 'name', 'is', 'kirill']
l2.sort()
print(l2)

# Example 11 - Sort reverse
l3 = ['hello', 'python', 'my', 'name', 'is', 'kirill']
l3.sort(reverse=True)
print(l3)

# Example 12 - Copy
l3.copy()
print(l3)

# Example 13 - Clear
l3.clear()
print(l3)