import random
#создаём пустой list
my_list = []
#переменная для итератора
i = 0
#заполняем list десятью случайными числами от 1 до 100
while i < 10:
    char = random.randint(1, 100)
    my_list.append(char)
    i += 1
#сортируем list по возростанию
my_list.sort()
#выбираем последнее значение
biggest_char = my_list[-1]
print(biggest_char)
