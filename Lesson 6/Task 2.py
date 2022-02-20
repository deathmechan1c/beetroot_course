import random
#создаём два пустых list
list_1 = []
list_2 = []
#переменная для итератора
i = 0
#заполняем list десятью случайными числами от 1 до 100
while i < 10:
    char_1 = random.randint(1, 10)
    char_2 = random.randint(1, 10)
    list_1.append(char_1)
    list_2.append(char_2)
    i += 1
#соибраем два list в set
list_unique = set(list_1 + list_2)
print(list_unique)