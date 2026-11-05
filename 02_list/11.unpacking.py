# first_name = "John"
# last_name = "Doe"
# age = 33

first_name, last_name, age = "John", "Doe", 33
print(first_name, last_name, age)

# data swap
a = 10
b = 20
# tmp = a
# a = b
# b = tmp
a, b = b, a
print(a, b)

# unpacking string
abc = "abc"
a, b, c = abc
print(a, b, c)

# unpacking lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, *_, last = numbers
print(first, last)
