#импортируем либу для радомной выборки символов из строки
import random
#инициализируем переменные для цикла
count = 0
random_string_data = ''
char_collector = ''
#переменная для условия задачи
string_lenght_static = 5
#запрос ввода данных
user_string = input('Введите строку: ')
#расчёт длины строки и проверка валидности к условию задачи
string_lenght = len(user_string)
#
if string_lenght < string_lenght_static :
    print('Введите строку длиннее, чем', string_lenght_static , 'символов')
else :
#цикл выборки случайного знака из строки, конкатенация символов в переменную-накопитель
    while count != string_lenght_static :
        char_collector = random.choice(user_string)
        random_string_data = random_string_data + char_collector
        count += 1
#вывод решения
print(random_string_data)