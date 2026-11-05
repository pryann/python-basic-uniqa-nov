yearly_salaries = [56_000, 72_000, 98_000, 61_000, 44_000, 76_000, 109_000]
high_salary_threshold = 75_000
high_salaries = []
summa_low_salaries = 0
summa_high_salaries = 0

for salary in yearly_salaries:
    if salary > high_salary_threshold:
        high_salaries.append(salary)
        summa_high_salaries += salary
    else:
        summa_low_salaries += salary

print(high_salaries)
print(summa_low_salaries)
print(summa_high_salaries)
