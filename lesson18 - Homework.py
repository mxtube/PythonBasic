"""
Lesson 18 - Homework
04.05.2023 @ Kirill Kuznetsov
"""
import sys

some_numbers = [1, 2, 3]

# Homework 1
print('Homework 1 - Дан список. Получите новый список, в котором каждое значение будет удвоено:')
new_numbers = [i * 2 for i in some_numbers]
print(new_numbers)

# Homework 2
print('Homework 2 - Дан список. Возведите в квадрат каждый из его элементов и получит список всех полученных квадратов:')
new_numbers2 = [i ** 2 for i in some_numbers]
print(new_numbers2)
answer: int  = 0
for i in new_numbers2:
    print(f'{answer} + {i} = {answer + i}')
    answer += i
else:
    print('Answer: %s' % answer)

# Homework 3
print('Homework 3 - Игорь любит кататься на велосипеде. Он знает, что при этом важно не допустить обезвоживания и '
      'пьет 0,5 литра воды в час. Вам дается время в часах, и вам нужно вернуть количество литров, которое игорь '
      'выпьет, с округлением до наименьшего значения:')
liters: float = 0.5
time: float = float(input('Enter hour: '))
print(f'Answer: {time} * {liters} = {int(time * liters)}')

# Homework 4
print('Homework 4 - Дана строка \'Hello world\'. Проверьте, если в этой строке есть символ проблема - " ", '
      'тогда преобразуйте строку к верхнему регистру, если же нет, тогда к нижнему:')
s = 'Hello world!'
for i in s:
    if i == ' ':
        s = s.upper()
    else:
        s = s.lower()
else:
    print(s)