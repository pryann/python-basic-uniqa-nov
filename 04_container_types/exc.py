# Adott egy string, amely szóközöket is tartalmaz. Írj egy függvéyny, amely eltávolítja a szóköz karaktereket a paraméterként lkapottstringből, majd a string karaktereit fordított sorrendben adja vissza! #}


def remove_space(text):
    return text.replace(" ", "")[::-1]


print(remove_space("a b c"))


#  Adottk egy paraméterként kapott lista, amely számokat tartalmaz. rj egy függvényt, amely visszaadja a lista elemeinek szorzatát!
def multi(numbers):
    mul = 1
    for i in numbers:
        mul *= i
    return mul


print(multi([1, 2, 3, 4, 5]))

#  Adott egky paraméterként kapott lista, amely számokat tartalmaz.
# Írj egy függvényt, amely visszaadja a lista elemeinek összegét a következő feltételek szerint: ha az elem pozitív, akkor az összegbe kerüljön be, ha negatív, akkor ne! #}


def summa(numbers):
    # summa = 0
    # for i in numbers:
    #     if i > 0:
    #         summa += i
    # return summa
    return sum(i for i in numbers if i > 0)


print(summa([-1, -2, -3, 1, 2, 3]))
