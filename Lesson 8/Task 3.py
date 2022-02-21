def make_operation(operator, *numbers):
    if operator == '+':
        return sum(numbers)
    elif operator == '-':
        return numbers[0] - sum(numbers[1:])
    elif operator == '*':
        index = 1
        for char in numbers:
            index = index * char
        return  index

numbers = []
number = None
while number:
    number = input('Введите число. Для завершения введите Stop: ')
    numbers.append(number)
    print('Вы ввели числа', numbers)
result = make_operation(input('Введите действие: '), numbers)
print(result)
