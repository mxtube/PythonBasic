"""
Lesson 30 - My Module
06.05.2023 @ Kirill Kuznetsov
"""

def get_count(string, symbol):
    counter = 0
    for i in string:
        if i == symbol:
            counter += 1
    return counter


def get_len(string):
    counter = 0
    for i in string:
        counter += 1
    return counter


if __name__ == '__main__':
    print('Hello, I am libs.py')