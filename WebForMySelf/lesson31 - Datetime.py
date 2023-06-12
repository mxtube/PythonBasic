"""
Lesson 31 - Module DateTime
07.05.2023 @ Kirill Kuznetsov
"""

from datetime import date, datetime, timedelta
import locale

# Example 1 - Date
today = date.today()  # Get date today 2023-05-07
print(today)
print(today.day)  # Get current date - 07
print(today.month)  # Get current month - 05
print(today.year)  # Get current year - 2023
print(today.weekday())  # Return day of week as an integer

# Example 2 - Datetime
now = datetime.now()
now2 = datetime.today()
print(now, now2, sep='\n')  # 2023-05-07 12:17:22.568003
print(now.day)  # Get current date - 7
print(now.month)  # Get current month - 5
print(now.year)  # Get current year - 2023
print(now.weekday())  # Return day of week as an integer

print(now.hour)  # 12
print(now.minute)  # 18
print(now.second)  # 59

days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
print(days[now.weekday()])  # Вс

# Example 3 - strftime
now3 = datetime.now()
print(now3)
print(now3.strftime('%a'))
print(now3.strftime('%A'))

locale.setlocale(locale.LC_ALL, 'ru_RU')
print(now3.strftime('%a'))
print(now3.strftime('%A'))
print(f'Date: {now3.strftime("%A, %d %b %Y")}')
print(f'Time: {now3.strftime("%H:%M:%S")}')

print(now.strftime('%c'))
print(now.strftime('%x'))
print(now.strftime('%X'))

# Example 4 - Time Delta
now4 = datetime.today()
print(now.strftime('%c'))
d1 = now + timedelta(days=30, hours=2, minutes=10)
print(d1.strftime('%c'))

