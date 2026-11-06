# print
# type
# id
# int
# float
# bool
# str
# input

print(dir(__builtins__))


def greetings(name):
    return f"Hi {name}!"


# greetings("John")
# greetings("Jane")
# greetings("Jack")
print(greetings("Me"))


def calculate_gross_price(price, vat_multiplier=1.27):
    return price * vat_multiplier


print(calculate_gross_price(1000))
print(calculate_gross_price(2000))
print(calculate_gross_price(10_000))
gross_price = calculate_gross_price(500, 1.05)
print(gross_price)


def add_item_to_basket(item, shopping_cart=None):
    if shopping_cart is None:
        shopping_cart = []
    shopping_cart.append(item)
    return shopping_cart


basket = []
# print(add_item_to_basket("apple", basket))
# print(add_item_to_basket("banana", basket))
# print(add_item_to_basket("orange", basket))
# print(basket)
print(add_item_to_basket("apple"))
print(add_item_to_basket("banana"))
print(add_item_to_basket("orange"))
