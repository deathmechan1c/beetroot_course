import random
playground = {a: 0 for a in range(64)}
print(playground)

bombs_indexes = []
i = 0
while i <= 10:
    cell_index = random.randint(0, 64)
    bombs_indexes.append(cell_index)
    i += 1
print(bombs_indexes)

for a in bombs_indexes :
    playground[a] = 1
    a += 1

print(playground)

user_cell = input('Введите номер ячейки для разминирования')
abc = playground.get(user_cell)
if abc == user_cell: