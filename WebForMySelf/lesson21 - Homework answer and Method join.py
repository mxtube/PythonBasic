"""
Lesson 21 - Homework. Answer
05.05.2023 @ Kirill Kuznetsov
"""

# Homework
"""
Дан список words. Составьте из него список слов-палиндромов.
Попробуйте это сделать двумя способами: произвольное решение и решение в одну строчку кода.
Дан список my_str со строками, часть из которых являются палиндромами. Составьте новый список строк-палиндромов.
"""
words = ['мадам', 'топот', 'test', 'madam', 'word', 'шалаш', 'око', 'дружба']
my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']

# Answer 1 - 1
print('Answer 1 - 1')
print([i for i in words if i[::-1].lower() == i.lower()])

# Answer 1 - 2
print('Answer 1 - 2')
palindromes = []
for word in words:
    if word == word[::-1]:
        palindromes.append(word)
else:
    print(palindromes)


# Answer 3 - by Antony

print("Answer 1 - 3")

my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
words = ['мадам', 'топот', 'test', 'madam', 'word', 'шалаш', 'око', 'дружба']

print(*filter(lambda x: x[::-1] == x, words))
print(*filter(lambda x: "".join(x.lower().split()) == "".join(x.lower().split())[::-1], my_str))

# Answer 2 - 1
print('Answer 2 - 1')
palindromes2 = []
for word in my_str:
    str_r = word.replace(' ', '').lower()
    if str_r == str_r[::-1]:
        palindromes2.append(word)
else:
    print(palindromes2)

"""
Lesson 21 - Method Join
05.05.2023 @ Kirill Kuznetsov
"""
print('Method Join')
some_list = list(range(1, 10))
some_list_symbols = list('python')

print(some_list)
print(some_list_symbols)

s = '-'.join(map(str, some_list))
s2 = ','.join(some_list_symbols)

print(s)
print(s2)