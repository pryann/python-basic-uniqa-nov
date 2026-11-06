# unordered
# contains  unique elements
# can  contains any type  of data

my_set = {1, 2, 3}

my_set.add(4)
print(my_set)

my_set.update([5, 6, 7])
print(my_set)

# raise an error if value does not exists
my_set.remove(4)
print(my_set)

my_set.discard(40)
print(my_set)

# remove a random element
my_set.pop()
print(my_set)

x1 = {"a", "b", "c"}
x2 = {"b", "c", "d"}

print(x1.union(x2))
print(x1.intersection(x2))
print(x1.difference(x2))
print(x1.symmetric_difference(x2))
print({"b"}.isdisjoint(x2))
print(x1.issubset({"a", "b", "c", "d"}))
print(x1.issuperset({"a", "b"}))

nums = [1, 2, 3, 2, 3, 4, 1, 3, 4]
unique_nums = list(set(nums))
print(unique_nums)

l1 = [1, 2, 3, 4, 1, 2, 3, 4]
l3 = [2, 3, 4, 2, 3, 4, 5, 5]
uniq = list(set(l1))
print(uniq)

l_union = list(set(l1).intersection(l3))
print(l_union)
