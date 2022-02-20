import datetime
# Функція “Завершення роботи” (номер 0). Виводить користувачеві повідомлення про закінчення роботи і завершує виконання програми.

# Функція “Створити нову задачу” (номер 1). Під час виконання функції користувачеві пропонується по черзі ввести значення
# для кожного з полів задачі. Якщо дані введено корректно, нова задача створюється та додається до загального списку, \
# користувачеві виводиться повідомлення про успішність дії. Якщо під час створення виникла помилка - користувач бачить відповідне повідомлення.
# Значення поля status при створенні у користувача не запитується, а автоматично встановлюється у значення ‘pending’.

# Функція ‘Переглянути список задач’ (номер 2). При виконанні цієї функції користувачеві виводяться всі задачі, що існують,
# відсортовані за значенням поля id. Вивод у форматі “{id} {title} {status}”.

# Функція “Переглянути деталі задачі” (номер 3). Користувач отримує запрошення ввести значення id задачі, яка його цікавить.
# Якщо задачі з таким id не існує, користувач отримує повідомлення про помилку.
# Якщо задачу знайдено - користувач бачить значення всіх полів цієї задачі.

# Функція “Редагувати задачу” (номер 4). Користувач отримує запрошення ввести значення id задачі, яку він хоче редагувати.
# Якщо задачі з таким id не існує, користувач отримує повідомлення про помилку.
# Якщо задачу знайдено - користувачеві по черзі пропонується ввести нові значення для кожного з полів задачі, включно з полем status.
# Якщо для якогось поля користувач не ввів нові дані - використовуємо старе значення для цього поля.
# Після оновлення задачі, користувачеві виводиться повідомлення про успішну операцію.
# У разі, якщо користувач ввів не валідне значення для певного поля - він отримує повідомлення про помилку і задача не оновлюється.

# Функція “Видалити задачу” (номер 5). ористувач отримує запрошення ввести значення id задачі, яку він хоче видалити.
# Якщо задачі з таким id не існує, користувач отримує повідомлення про помилку.
# Якщо задачу знайдено - вона видаляється із загального списку.
#
from datetime import date
task = list(task_id, title, decription, priority, status, due_date)

def make_task():
    while True:
        try:
            answer1 = int(input('Type id of task (from 1 to 10)'))
            break
        except ValueError as err:
            if not 1 <= answer1 <= 10:
                print(err, 'Type id task from 1 to 10')
        except TypeError as err:
            print(err, 'Type in digit form')
    while True:
        try:
            answer2 = input('Type name of the task')
            break
        except ValueError as err:
            if len(answer2) == 0:
                print(err, 'Type name of task')
        except TypeError as err:
            print(err, 'Type a string')

    answer3 = input('Type decription of the task')
    while True:
        try:
            answer4 = int(input('Type priority of task (from 1 to 10)'))
            if len(answer4) == 0:
                answer4 = 1
            break
        except ValueError as err:
            if not 1 <= answer4 <= 10:
                print(err, 'Type priority task from 1 to 10')
        except TypeError as err:
            print(err, 'Type in digit form')
    task[4] = 'pending'
    while True:
        try:
            answer2 = input('Type date of the end of the task in format DD.MM.YYYY: ')
            day_str, month_str, year_str = answer2.split('.')
            date(day=int(day_str), month = int(month_str), year = int(year_str))


            break
        except ValueError as err:
            if len(answer2) == 0:
                print(err, 'Type name of task')
        except TypeError as err:
            print(err, 'Type a string')


#answer2.strftime('%b/%d/%Y')