#хардкодим переменную длины номера мобильного телефона
phone_number_lenght_default = 10
#просим пользователя ввести номер
phone_number = input('Введите номер мобильного телефона: ')
#инструкция для работы программы
#номер будет валидным, только если оба условия выполняются
if len(phone_number) == phone_number_lenght_default and phone_number.isdigit() :
    print('Номер мобильного телефона валидный ')
else :
    print('Введённый номер мобильного телефона должен быть длиной в 10 символов и состоять из цифр')