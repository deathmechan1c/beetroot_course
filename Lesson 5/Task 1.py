import random
#генерируем случайное число от 1 до 10
number = random.randint(1, 10)
#просим пользователя ввести число
user_number = int(input('Введите число от 1 до 10: '))
#создаём цикл для проверки ввода
if user_number < 1 or user_number > 10 :
    print('Вы ввели неверное число.')
#вложенный цикл для проверки условия
else:
    if number == user_number :
        print('Вы угадали.')
    else :
        print('Вы не угадали.')