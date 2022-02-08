#просим пользователя ввести массу и рост, конвертируем в float для удобства подсчёта
weight = float(input('Введите массу тела в кг. - '))
height = float(input('Введите рост в метрах - '))
#даём возможность пользователю проверить введённые данные
print('Вы ввели массу', weight, 'и рост', height)
#формула расчёта ИМТ
BMI = weight/(height ** 2)
#выводим значение ИМТ для пользователя с округлением до двух знаков после запятой
print('Ваш BMI равен ', format(BMI, '.2f'))
#задаём перемнные нижней и верхней границы ИМТ
lower_bound = 18.5
upper_bound = 25
#выводим сообщение для пользователя в зависимости от его ИМТ с помощью if-elif-else
if BMI < lower_bound :
    print('Your BMI is less than normal')
elif lower_bound < BMI < upper_bound :
    print('Your BMI is normal')
else :
    print('Your BMI is greater than normal')

