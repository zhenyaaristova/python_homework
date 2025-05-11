# задание 1
name = input('Введите имя: ')
age = int(input('Введите возраст: '))
if age < 0 or age > 130:
    print('Неверный возраст')
    exit(0)
question = input('Любите ли Вы программировать? ')
user_info = {
    "имя": name,
    "возраст": age,
    "любит ли программировать": question
}
print(user_info)

# задание 2
x = float(input('Введите Х:'))
y = float(input('Введите У:'))
print(y > x - 2)