#просим пользователя ввести данные о себе
name = input('Введите своё имя: ')
age = input('Введите свой возраст: ')
#проверяем данные на валидность. В случае невалидности закрываем программу.
if name.isdigit() or age.isalpha() :
    print('Вы ввели неверные данные. Попробуйте снова')
    exit()
#в случае валидности выводим сообщение
else :
    print('Hello,', name, ',', 'on your next birthday you’ll be', int(age) + 1)