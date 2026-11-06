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
