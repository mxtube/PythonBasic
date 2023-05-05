"""
Lesson 24 - Dictionary methods
05.05.2023 @ Kirill Kuznetsov
"""

# Example 1 - Basic
product = {'title': 'iPhone', 'price': 150}
print(product.items())
print(product.keys())

# Example 2 - Pop
new_product = product.pop('title')
print(new_product)

# new_product = product.pop('title2') # No good
# print(new_product2)

new_product = product.pop('title2', 'Not found')
print(new_product)

# Example 3 - Setdefault
product = {'title': 'iPhone', 'price': 150}
print(product)
print(product.setdefault('title'))
print(product.setdefault('title2', '🙈'))

# Example 4 - Update
product = {'title': 'iPhone', 'price': 150}
product.update({'year': 2023})
print(product)

product.update({'price': 170})
print(product)

# Example 5 - Values
product = {'title': 'iPhone', 'price': 170, 'year': 2023}
print(product.values())

# Homework
"""
Создайте игру "Угадай число". В коде программы в переменную запишите любое число от 1 до 100 
(в следующих уроках мы узнаем, как генерировать случаиное число), которое и должен угадать игрок. 
Далее программа должна спросить у игрока угадать число. Если пользователь не угадал число
- программа сооощает, что загаданное число оольшеменьше и предлагает попробовать еще
раз, при этом программа ведет счета кол-ва попыток игрока. 
Если игрок угадал число, тогда программа благодарит за игру и сообщает кол-во попыток, за которое было угадано число.
"""