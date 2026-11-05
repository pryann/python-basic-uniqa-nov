from tkinter import N


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[0])
print("from 2.: ", numbers[2:])
print("to 2.: ", numbers[:2])
print("from 2. to 6.: ", numbers[2:6])
print("from 2. to 8. step 2: ", numbers[2:8:2])
print("last element: ", numbers[-1])
print("second last element: ", numbers[-2])
print("reverse: ", numbers[::-1])

numbers_copy = numbers[:]
print(id(numbers), numbers)
print(id(numbers_copy), numbers_copy)

numbers[0:2] = ["first", "second"]
print(numbers)
