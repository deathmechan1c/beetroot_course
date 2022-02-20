#входные данные
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
#создаём функцию, с параметрами как наши словари
#на каждое значение ключа из stock мы перемножаем соответствующие ключам значения из двух словарей
def fruits(stock, prices):
    fruit_price = 0
    for key in stock:
        fruit_price += stock[key] * prices[key]
    return fruit_price
print(fruits(stock, prices))
