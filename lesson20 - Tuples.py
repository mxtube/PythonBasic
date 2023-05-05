"""
Lesson 20 - Tuples
04.05.2023 @ Kirill Kuznetsov
"""

# Example 1 - Basic
t1 = (1, 2, 3)
print(t1, type(t1))

# Example 2 - No good practice
t2 = 1, 2, 3
print(t2, type(t2))

# Example 3
t3 = tuple((1, 2, 3))
print(t3, type(t3))

# Example 4
t4 = ()
print(t4, type(t4))

# Example 5 - No good
t5 = ()
t5 = (1)
print(t5, type(t5))

# Example 6 - Good
t6 = ()
t6 = (1,)
print(t6, type(t6))

# Example 7
t7 = tuple('hello')
print(t7, type(t7))

# Example 8
t8 = tuple('hello')
print(t8[3], type(t8[3]))

# Example 9
l9 = [1, 2, 3]
t9 = (1, 2, 3, 3, 3, 3)
print(l9.__sizeof__())
print(t9.__sizeof__())

# Example 10
print(len(t9))
print(t9.count(3))
if 1 in t9:
    print(t9.index(1))

# Example 11
pyt = 'hello! python'
t11 = [i for i in pyt]
for i in t11:
    print(i, end=' ')
else:
    print('')

# Example 12
t12 = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'python'])
print(t12, id(t12))
t12[4][0] = 'new'
t12[4].append('world')
print(t12, id(t12))

# Example 13 - Unpack
t13 = (1, 2, 3)
x = t13[0]
y = t13[1]
z = t13[2]
print(x, y, z)

x, y, z = t13
print(x, y, z)

# Example 14
x = 1
y = 2
x, y = y, x
print(x, y)
