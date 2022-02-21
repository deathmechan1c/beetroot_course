#создаём пустой словарь
my_dictionary = {}
#создаём функцию, с параметрами name и capital
#где в словарь с ключом name вводится значение capital
#и словарь выводится на print
def make_country(name, capital):
    my_dictionary[name] = capital
    print(my_dictionary)
#вызываем функцию, передаём туда параметры из input'а
make_country(input('Country: '), input('Capital: '))