"""
Lesson 25 - Homework Game
05.05.2023 @ Kirill Kuznetsov
"""

import random

# Homework - My Game
"""
Создайте игру "Угадай число". В коде программы в переменную запишите любое число от 1 до 100
(в следующих уроках мы узнаем, как генерировать случаиное число), которое и должен угадать игрок.
Далее программа должна спросить у игрока угадать число. Если пользователь не угадал число
- программа сооощает, что загаданное число оольшеменьше и предлагает попробовать еще
раз, при этом программа ведет счета кол-ва попыток игрока.
Если игрок угадал число, тогда программа благодарит за игру и сообщает кол-во попыток, за которое было угадано число.
"""

hidden_number: int = None
user_answer: int = None
counter: int = 0
print('Welcome to Guess the Number', 'We guessed the number 🎲 from 1 to 100', sep='\n')

hidden_number = random.randrange(1, 101)
print('[DEBUG] Hidden number is', hidden_number)
counter += 1
user_answer = int(input('Enter your number: '))

while True:
    if user_answer > hidden_number:
        counter += 1
        print(f'Your number is greater. You try {counter}')
        user_answer = int(input('Enter your number: '))
    elif user_answer < hidden_number:
        counter += 1
        print('Your number is less, you. You try: %s' % counter)
        user_answer = int(input('Enter your number: '))
    elif user_answer == hidden_number:
        print('You win. You try: %s' % counter)
        break
    else:
        print('error')

# Homework - Answer
