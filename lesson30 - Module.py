"""
Lesson 30 - Module
06.05.2023 @ Kirill Kuznetsov
"""

import os
import libs
import random as r
from random import shuffle
from sys import *

# Example 1 - Get CWD (Current working directory)
print(os.getcwd())

# Example 2 - Get random number from 1 to 100
rand = r.randint(1, 100)
rand2 = r.randrange(1, 100)
print(rand, type(rand))
print(rand2, type(rand2))

# Example 3
l1 = [1, 2, 3, 4, 5]
shuffle(l1)
print(l1)

print(libs.get_count('abracadabra', 'a'))
print(libs.get_len('Kuznetsov'))

