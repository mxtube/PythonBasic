"""
Lesson 32 - Homework
07.05.2023 @ Kirill Kuznetsov
"""

import os

# tree = os.walk('papka')
# print(tree)
#
# for files in tree:
#     print(files)

def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        level = root.count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}[{os.path.basename(root)}]')
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            print(f'{subindent}{file}')
        # print(root, files, level, indent, subindent)

read_dir('papka')