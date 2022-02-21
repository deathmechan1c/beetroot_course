#Первый вариант
def favourite_movie():
    name = input('Введите название вашего любимого фильма: ')
    return name
print('My favorite movie is named', favourite_movie())
#Второй вариант
def favourite_movie(name):
    print('My favorite movie is named', name)
favourite_movie(input('Введите название вашего любимого фильма: '))