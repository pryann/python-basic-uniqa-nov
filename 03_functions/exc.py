# 1. Írj egy Python függvényt, amely visszaadja a paraméterként kapott stringben található szavak számát!


def get_word_counter(text):
    # texts = text.split()
    # length = len(texts)
    # return length
    return len(text.split())


print(get_word_counter("lorem ipsum dolor sit amet"))

# 2. Írj egy függvényt, amely egy számokat tartalmazó listát kap paraméterként, majd visszatér egy új listával, amelyben a számok duplája szerepel.


def get_doubled_values(numbers):
    # doubled = []
    # for i in numbers:
    #     doubled.append(i * 2)
    # return doubled

    return [i * 2 for i in numbers]


print(get_doubled_values([1, 2, 3, 4, 5]))
# 3. Írj egy Python függvényt, amely eldönti, hogy egy paraméterként kapott string palindrom-e vagy sem! Case insensitive!
# Használj slicingot!


def is_palindrom(text):
    # lowercase_text = text.lower()
    # lowercase_reverse = text[::-1].lower()
    # return lowercase_text == lowercase_reverse

    return text.lower() == text[::-1].lower()


print(is_palindrom("abbA"))
print(is_palindrom("baba"))


# 1. Készíts egy függvényt, amely paraméterként kap két listát és visszaadja azt a listát, amely csak azokat az elemeket tartalmazza, amelyek mindkét listában szerepelnek! Comprehensiont használj!
def get_intersection(list_1, list_2):
    # intersection = []
    # for i in list_1:
    #     if i in list_2:
    #         intersection.append(i)
    # return intersection

    return [i for i in list_1 if i in list_2]


# 2.  Készíts egy függvényt, amely meghatározza, hogy egy szám prím-e vagy sem!
# A függvény paraméterként egy számot kap a visszatérési érték pedig bool típusú érték.


def is_prime(number):
    if number < 2:
        return False

    #  you can optimize it
    for i in range(2, number):
        if number % i == 0:
            return False

    return True
