#просим пользователя ввести строку
string = input('Введите строку: ')
#берём первые и последние два символа в строке
string_slice_1 = string[0:2]
string_slice_2 = string[-2:]
#условие для работы программы
if len(string) < 3 :
    print('')
else :
    print(string_slice_1 + string_slice_2)