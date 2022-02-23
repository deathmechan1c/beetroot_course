#создаём функцию, в которой запрашиваем два числа
#проверяем переменные на уифры и на ноль
def my_function():
    try:
        a = int(input('Первое число: '))
        b = int(input('Второе число: '))
    except ValueError:
        print('Введите число')
    else:
        try:
            c = pow(a,2) / b
        except ZeroDivisionError:
            print('Нельзя делить на ноль')
        else:
            print(c)
my_function()