#создаём функцию для расчётов, куда первым параметром вводим действие,
#а далее - списком -числа
def make_operation(operator, numbers):
    if operator == '+':
        return sum(numbers)
    elif operator == '-':
        return numbers[0] - sum(numbers[1:])
    elif operator == '*':
        index = 1
        for char in numbers:
            index = index * char
        return  index
#создаём пустой список
numbers = []
#с помощью цикла заполняем список числами, пока пользователь не напишет Stop
while True :
    input_number = input('Введите число. Для завершения введите Stop:  ')
    if input_number == 'Stop':
        break
    numbers.append(int(input_number))
    print('Вы ввели числа', numbers)
#вызываем функцию, передаём параметр, вводя с клавиатуры, и список чисел
result = make_operation(input('Введите действие: '), numbers)
print(result)
