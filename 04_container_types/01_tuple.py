# ordered, indexed
# can contains duplicated elements
# can store any type of data
# IMMUTABLE

rgb = (255, 0, 0)
print(rgb[0])
# TypeError: 'tuple' object does not support item assignment
# rgb[0] = 0
print(rgb.index(255))
print(rgb.count(0))

nums = [
    1,
    2,
    3,
]

one_element_tuple = (1,)
print(type(one_element_tuple))


def stat(numbers):
    return min(numbers), max(numbers), sum(numbers)


statistic = stat([1, 2, 3, 4, 5, 6, 7, 8])
print(statistic, type(statistic))

print((1, 2, 3) + (4, 5, 6))
print((1, 2, 3) * 2)

for i in statistic:
    print(i)

