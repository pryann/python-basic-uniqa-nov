for i in range(10):
    print(i)

# for ciklusváltozó in adat:
#   ciklusmag

i = 0
while i < 10:
    print(i)
    i += 1

while True:
    grade = input("Adj meg egy osztályzatot (1-5): ")
    if grade.isdigit() and 0 < int(grade) < 6:
        print("Ez egy érdemjegy")
        break
    print("Ez NEM érdemjegy")
