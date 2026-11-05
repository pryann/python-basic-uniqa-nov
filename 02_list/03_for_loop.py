for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(10, 101, 10):
    print(i)

for i in range(10, 0, -1):
    print(i)

yearly_salaries = [56_000, 72_000, 98_000, 61_000]
for yearly_salary in yearly_salaries:
    print(yearly_salary)

# for i in range(len(yearly_salaries)):
#     print(i, yearly_salaries[i])

for i, v in enumerate(yearly_salaries):
    print(i, v)
