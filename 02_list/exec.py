# BASIC SOLUTIONS

# Írj egy Python programot, amely eltávolítja az összes ismétlődő elemet egy listából és kiírja az eredményt!

items = [1, 2, 3, 4, 2, 3, 1, 1, 2, 5, 4]
unique_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)

print(unique_items)

# items = list(set(items))
# print(items)

# Írj egy Python programot, amely kiírja a listában található összes számot, ami 3-mal vagy 4-gyel vagy 5-tel osztható!
for item in items:
    if item % 3 == 0 or item % 4 == 0 or item % 5 == 0:
        print(item)

# Írj egy Python programot, amely egy listából az összes páros és páratlan számot két külön listába szétválasztja!
even = []
odd = []
for item in items:
    if item % 2 == 0:
        even.append(item)
    else:
        odd.append(item)

print(even)
print(odd)
