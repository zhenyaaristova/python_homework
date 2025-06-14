# задача 1
# 1. Получить текст от пользователя
# 2. Подсчитать количество гласных и согласных букв
# 3. Найти самое длинное слово
# 4. Подсчитать количество вхождений заданного слова
from idlelib.replace import replace
#
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
#
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