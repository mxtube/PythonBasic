"""
Lesson 17 - Mutable and immutable objects
02.05.2023 @ Kirill Kuznetsov
"""

# Example 1
x = 10
print(x, id(x))
x = 20
print(x, id(x))

# Example 2
s = 'hello'
print(s, id(s))
s += ' python'
print(s, id(s))

# Example 3
l1 = [1, 2, 3]
print(l1, id(l1))
l1.append(5)
print(l1, id(l1))

# Example 4
x = 10
y = x
print(x, id(x))
print(y, id(y))

x = 15
print(x, id(x))
print(y, id(y))

# Example 5
l1 = [1, 2, 3]
l2 = l1
print(l1, id(l1))
print(l2, id(l2))

l1.append(6)
print(l1, id(l1))
print(l2, id(l2))

l2.append(7)
print(l1, id(l1))
print(l2, id(l2))

# Example 6
l3 = l2[:]
print(l2, id(l2))
print(l3, id(l3))

# Example 7
a = 10
print(a)
del a
print(a)