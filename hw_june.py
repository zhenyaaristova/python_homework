# задача 1
# 1. Получить текст от пользователя
# 2. Подсчитать количество гласных и согласных букв
# 3. Найти самое длинное слово
# 4. Подсчитать количество вхождений заданного слова

# string = input('Введите текст: ')
# text = string.upper()
# vowels = 'АОУЫИЭЕЁЮЯ'
# count_v = 0
# count_c = 0
# for x in text:
#     if x.isalpha():
#         if x in vowels:
#              count_v += 1
#         else:
#              count_c += 1
# print(f'Количество гласных букв: {count_v}')
# print(f'Количество согласных букв: {count_c}')
#
# words = string.split()
# max_word = ''
# for w in words:
#     clean_word = ''
#     for c in w:
#         if c.isalpha():
#             clean_word += c
# if len(clean_word) > len(max_word):
#     max_word = clean_word
# print(f'Самое длинное слово: {max_word}')
#
# search_word = input('Введите слово для поиска: ')
# nmlz_word = []
# for w in words:
#     clean = ''.join([c for c in w if c.isalpha()])
#     nmlz_word.append(clean)
# print(f'Количество вхождений слова: {nmlz_word.count(search_word)}')

# задача 2
# Напишите программу, которая принимает строку и
# удаляет из нее все пробелы.

# def string(s):
#     return s.replace(' ', '')
# str = input('Введите строку: ')
# result = string(str)
# print(result)

# задача 3
# Напишите программу, которая принимает строку и
# выводит на экран самое длинное слово в ней.

# string = input('Введите строку: ').split()
# max_word = ''
# for w in string:
#     clean_word = ''
#     for c in w:
#         if c.isalpha():
#             clean_word += c
# if len(clean_word) > len(max_word):
#     max_word = clean_word
# print(f'Самое длинное слово: {max_word}')

# задача 4
# Написать процедуру на Python, которая принимает имя
# пользователя в качестве входных данных, выводит
# персонализированное приветствие и сообщает общее
# количество символов в этом имени (без учета
# пробелов).

# def greet_and_count(user_name):
#     print(f'Привет, {user_name}! Добро пожаловать!')
# name = input('Введите имя пользователя: ')
# greet_and_count(name)
#
# count = 0
# for x in name:
#     if x.isalpha():
#         count += 1
# print(f'Количество букв в твоем имени (без учетов пробелов): {count}')

# задача 5
# Напишите функцию, которая вычисляет среднее
# арифметическое пяти целых чисел.

# def am(n1, n2, n3, n4, n5):
#     return (n1 + n2 + n3 + n4 + n5)/5
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = int(input('Введите третье число: '))
# num4 = int(input('Введите четвертое число: '))
# num5 = int(input('Введите пятое число: '))
# result = am(num1, num2, num3, num4, num5)
# print(f'Среднее арифметическое введенных чисел: {result}')

# задача 6
# Напишите функцию, которая находит количество
# цифр в десятичной записи числа.

# def nums(n):
#     return len(str(n))
# num = int(input('Введите целое число: '))
# result = nums(num)
# print(f'Количество цифр в числе: {result}')

# задача 7
# Найти периметр треугольника, заданного
# координатами своих вершин.
