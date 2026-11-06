# min, max, summa, count, decision, select


def get_minimum(numbers):
    if not numbers:
        raise ValueError("The lsit is empty")

    minimum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
    return minimum


numbers = [1, 2, 3, 4, 5, 6, 0]
print(get_minimum(numbers))
print(min(numbers))


def get_maximum(numbers):
    if not numbers:
        raise ValueError("The list is empty")

    maximum = numbers[0]
    for num in numbers[1:]:
        if num > maximum:
            maximum = num
    return maximum


numbers = [1, 2, 3, 4, 5, 6, 0]
print(get_maximum(numbers))
print(max(numbers))


def summa(numbers):
    summa = 0
    for i in numbers:
        summa += i
    return summa


print(summa(numbers))
print(sum(numbers))


def average(numbers):
    return summa(numbers) / len(numbers)


print(average(numbers))


def count_values(numbers, search):
    counter = 0
    for i in numbers:
        if i == search:
            counter += 1
    return counter


print(count_values(numbers, 1))
print(numbers.count(1))


# kiválasztás, tudjuk h benne van, az index kell


def get_index(numbers, search):
    for i, v in enumerate(numbers):
        if v == search:
            return i


print(get_index(numbers, 4))
print(numbers.index(4))

#  eldöntés : True  - False


def decision(numbers, search):
    for i in numbers:
        if i == search:
            return True
    return False


print(decision(numbers, 3))
print(3 in numbers)
