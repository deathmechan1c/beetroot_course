#создаём статичную переменную для имени
MY_NAME = 'vadim'
#просим пользователя ввести его имя
my_name = input('Введи своё имя: ')
#создаём условие программы - если введённое имя равно сохранённому или введённое имя, обращённое в нижний регистр
#равно сохранённому, то имена совпадают
if my_name == MY_NAME or (my_name.lower() == MY_NAME) :
    print('Введённое имя совпадает')
else :
    print('Введённое имя не совпадает')