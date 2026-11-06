from random import choice, randint, shuffle

print(randint(1, 100))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(nums)
print(nums)

print(choice(nums))
