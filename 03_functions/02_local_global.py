price = 1000

print(price)


def log_price():
    global price
    price = 1111
    print(price)


log_price()

print(price)

