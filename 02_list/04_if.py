yearly_salary = 100_000
high_salary_threshold = 100_000

print(True, type(True))
print(False, type(False))

# ==, !=, <, >, <=, >=, is, is not, in, not in
if yearly_salary > high_salary_threshold:
    print("High salary")
else:
    print("Low salary")


grade = input("Adj megy egy osztályzatot (1-5): ")
if grade == "1":
    print("Elégtelen")
elif grade == "2":
    print("Elégséges")
elif grade == "3":
    print("Közepes")
elif grade == "4":
    print("Jó")
elif grade == "5":
    print("Jeles")
else:
    print("Ez nem osztályzat")
