weight = float(input('Введите массу тела в кг. - '))
height = float(input('Введите рост в метрах - '))
print('Вы ввели массу', weight, 'и рост', height)
BMI = weight/(height ** 2)
print('Ваш BMI равен ', format(BMI, '.2f'))
lower_bound = 18.5
upper_bound = 25
BMI_status = lower_bound < BMI < upper_bound
print('Your BMI is normal:', BMI_status)
