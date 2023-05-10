"""
Lesson 39 - Class parsing
10.05.2023 @ Kirill Kuznetsov
"""

from parser_class import Parser

parser = Parser(url='https://kp11.mskobr.ru/o-nas/pedagogicheskii-sostav', path='teacher.txt')

parser.run()
print(parser.result)
