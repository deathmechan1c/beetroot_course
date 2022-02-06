country_phone_number_prefix = '380'
#
phone_number = input('Введите номер мобильного телефона: ')
print('Вы ввели номер', phone_number)
#
phone_number_lenght = len(phone_number)
check_phone_number_lenght = phone_number_lenght == 12
print('Длина номера мобильного телефона', phone_number_lenght, 'символов')
print('Длина номера мобильного телефона валидна?', check_phone_number_lenght)
#
check_phone_number_is_digits = phone_number.isdigit()
print('Номер телефона состоит из цифр?', check_phone_number_is_digits)
#
phone_number_prefix = phone_number[0:3]
print('Префикс введённого номера:', phone_number_prefix)
#
check_phone_number_prefix = phone_number_prefix == country_phone_number_prefix
print('Префикс введённого номера валидный: ', check_phone_number_prefix)
#
whole_phone_number_is_vaild = (check_phone_number_lenght == True and check_phone_number_is_digits == True and check_phone_number_prefix == True)
#
print('Введённый номер телефона валидный: ', whole_phone_number_is_vaild)