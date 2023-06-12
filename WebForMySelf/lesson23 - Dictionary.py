"""
Lesson 23 - Dictionary
05.05.2023 @ Kirill Kuznetsov
"""

# Example 1 - Create empty dictionary
dict1 = {}
print(dict1, type(dict1))

# Example 1 - Create example
product = {
    'title': 'Apple',
    'price': 150
}
print(product, type(product))

# Example 2 - Create with constructor
product2 = dict(title='iPhone', price=13000)
print(product2, type(product2))

# Example 3 - Dictionary conversion
users = [
    ['bob@gmail.com', 'Bob'],
    ['julia@mail.ru', 'Julia'],
    ['john@mail.com', 'John']
]
print(users, type(users))
d_users = dict(users)
print(d_users, type(d_users))

users2 = (
    ('bob@gmail.com', 'Bob'),
    ('julia@mail.ru', 'Julia'),
    ('john@mail.com', 'John')
)
print(users2, type(users2))
d_users = dict(users2)
print(d_users, type(d_users))

# Example 4 - From Keys
product4 = dict.fromkeys(['price1', 'price2', 'price3'], 50)
print(product4, type(product4))
product4 = dict.fromkeys(['price1', 'price2', 'price3'])
print(product4, type(product4))

# Example 5 - Generator
nums = {i: i + 3 for i in range(20, 30)}
print(nums)

# Example 6 - Get item from dict
product62 = product = {'title': 'Apple', 'price': 150}
product61 = dict(title='iPhone', price=13000)
print(product62["title"])

# Example 7 - Method get
product72 = product = {'title': 'Apple', 'price': 150}
product71 = dict(title='iPhone', price=13000)
print(product72.get('title'))
print(product72.get('title2'))
print(product72.get('title2', 'Not found')) # if no key

# Example 8 - Loop
product8 = {'title': 'Apple', 'price': 150}
# for key in product8:
#     print(key, end=' ')
#     print(product8[key], end=' ')
#     print(f'  {key} : {product8[key]}')

print(product8.items())
for key, value in product8.items():
    print(key, type(key), value, type(value))

# Example 9
products = [
    {'title': 'iPhone', 'price': 150},
    {'title': 'Macbook', 'price': 210},
    {'title': 'Apple Watch', 'price': 40}
]
print(products, type(products))
for product in products:
    print(product)
    print(product['title'], type(product['title']), product['price'], type(product['price']))