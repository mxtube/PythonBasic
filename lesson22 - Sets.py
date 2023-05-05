"""
Lesson 22 - Sets
05.05.2023 @ Kirill Kuznetsov
"""

# Example 1
set1 = {'apple', 'orange', 'apple', 'raspberry', 'orange', 'pineapple'}
print(set1, type(set1))

# Example 2
set2 = set('python')
print(set2, type(set2))

# Example 3
set3 = {i for i in range(1, 11)}
print(set3)

# Example 4
set4 = {}
print(set4, type(set4))

set41 = set()
print(set41, type(set41))

# Example 5
nums = [1, 2, 3, 4, 4, 2, 4, 5]
nums2 = set(nums)
print(nums2, type(nums2))

# Example 6 - Subtraction
a = set('abracadabra')
b = set('alacazam')

print(a, b, sep='\n')

c = a - b # Subtraction - removes from a all the letters that are in b
print(c)

# Example 7 - Union
a = set('abracadabra')
b = set('alacazam')

d = a | b  # Union - letters either in a or in b

print(d)

# Example 8 - Intersection
a = set('abracadabra')
b = set('alacazam')
e = a & b # Intersection - letters in both a and b
print(e)

# Example 9 - Set of elements
a = set('abracadabra')
b = set('alacazam')

f = a ^ b # Set of elements - letters in a or b, but not in both

print(f)

"""
Lesson 22 - Sets Methods
05.05.2023 @ Kirill Kuznetsov
"""

set1 = {'apple', 'orange', 'apple', 'raspberry', 'orange', 'pineapple'}

# Example 1 - Copy set.copy() - Return set copy
s2 = set1.copy()
print(set1, id(set1))
print(s2, id(s2))

# Example 2 - set.add() - Add new element
s2.add('banana')
print(s2, id(s2))

# Example 3 - set.remove() - Remove element from set
s2.remove('banana')
print(s2, id(s2))

# s2.remove('banana') No good
print(s2, id(s2))

s2.discard('banana')
print(s2, id(s2))

# Example 4 - set.pop
# Example 5 - set.clear()
s2.clear()
print(s2, id(s2))

# Example 6 - Frozenset
a = frozenset('hello')
print(a, type(a))