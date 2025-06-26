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
#
# def distance(x1, y1, x2, y2):
#     return (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
# def trngl_per(x1, y1, x2, y2, x3, y3):
#     a = distance(x1, y1, x2, y2)
#     b = distance(x2, y2, x3, y3)
#     c = distance(x3, y3, x1, y1)
#     return a + b + c
# print(trngl_per(1, 2, 4, 5, 6, 7))

# задача 19
# def pointInRect(x, y, x1, y1, x2, y2):
#     return x1 <= x <= x2 and y2 <= y <= y1
#
# x = int(input('Введите координату х исходной точки: '))
# у = int(input('Введите координату у исходной точки: '))
# x1 = int(input('Введите координату х левого верхнего угла прямоугольника: '))
# у1 = int(input('Введите координату у левого верхнего угла прямоугольника: '))
# x2 = int(input('Введите координату х правого нижнего угла прямоугольника: '))
# у2 = int(input('Введите координату у правого нижнего угла прямоугольника: '))
#
# print(pointInRect(x, y, x1, y1, x2, y2))

# задача 20
# def side_len(x1, y1, x2, y2):
#     return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#
# def tri_area(a, b, c):
#     p = (a + b + c)/2
#     return (p * (p - a) * (p - b) * (p - c))**0.5
#
# def pointInTriangle(px, py, x1, y1, x2, y2, x3, y3):
#     a = side_len(x1, y1, x2, y2)
#     b = side_len(x2, y2, x3, y3)
#     c = side_len(x3, y3, x1, y1)
#     area_abc = tri_area(a, b, c)
#
#     a1 = side_len(px, py, x1, y1)
#     b1 = side_len(px, py, x2, y2)
#     c1 = side_len(x1, y1, x2, y2)
#     area_pab = tri_area(a1, b1, c1)
#
#     a2 = side_len(px, py, x2, y2)
#     b2 = side_len(px, py, x3, y3)
#     c2 = side_len(x2, y2, x3, y3)
#     area_pbc = tri_area(a2, b2, c2)
#
#     a3 = side_len(px, py, x3, y3)
#     b3 = side_len(px, py, x1, y1)
#     c3 = side_len(x3, y3, x1, y1)
#     area_pca = tri_area(a3, b3, c3)
#
#     total_area = area_pab + area_pbc + area_pca
#     # return abs(total_area - area_abc) < 1e-5
#     return round(total_area, 5) == round(area_abc, 5) # округление
#
# print(pointInTriangle(1, 1, 0, 0, 4, 0, 0,3))

# задача 21
# def a(score):
#     sorted_scores = sorted(score)
#     remains = sorted_scores[1: -1]
#     point = sum(remains)/3
#     return point
# result = a([5, 10, 100, 50, 6])
# print(f'Итоговая оценка: {result}')

