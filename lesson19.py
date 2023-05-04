"""
Lesson 19 - Homework. Answer
04.05.2023 @ Kirill Kuznetsov
"""

some_numbers = [1, 2, 3]

# Homework 1
print('Homework 1 - Дан список. Получите новый список, в котором каждое значение будет удвоено:')
print('Answer:', [i * 2 for i in some_numbers])

# Homework 2
print(
    'Homework 2 - Дан список. Возведите в квадрат каждый из его элементов и получит список всех полученных квадратов:')
res = 0
for num in some_numbers:
    res += num ** 2
print(res)

# Homework 3
print('Homework 3 - Игорь любит кататься на велосипеде. Он знает, что при этом важно не допустить обезвоживания и '
      'пьет 0,5 литра воды в час. Вам дается время в часах, и вам нужно вернуть количество литров, которое игорь '
      'выпьет, с округлением до наименьшего значения:')
time1 = 3       # litres = 1
time2 = 6.7     # litres = 3
time3 = 11.8    # litres = 5

print(int(time1 // 2))
print(int(time2 // 2))
print(int(time3 // 2))

print(int(time1 / 2))
print(int(time2 / 2))
print(int(time3 / 2))

# Homework 4
print('Homework 4 - Дана строка \'Hello world\'. Проверьте, если в этой строке есть символ проблема - " ", '
      'тогда преобразуйте строку к верхнему регистру, если же нет, тогда к нижнему:')

s = 'Hello world'
if ' ' in s:
    s = s.upper()
else:
    s = s.lower()
print(s)
