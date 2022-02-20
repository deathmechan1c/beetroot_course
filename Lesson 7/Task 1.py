#создаём пустой словарь
my_dict = {}
#просим пользователя ввести строку
my_string = input('Введите строку: ')
#разбиваем строку на слова, кладём в список
words_list = my_string.split()
#цикл проверки: если слово есть в словаре, сделать инкремент значения
#если нет - как новый ключ со значением "1"
for word in words_list:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1
print(my_dict)
