def oops():
    try:
        a = [1,2]
        print(a[3])
    except IndexError:
        print('Это ошибка!')
        raise
oops()
###############################
def oops_2():
    try:
        oops()
    except IndexError:
        print('Опять ошибка!')
oops_2()
