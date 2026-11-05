# list is not typed, can contains any type of  data
# allow duplicated member
# order  - indexed
# mutable

yearly_salaries = [56_000, 72_000, 98_000, 61_000]
print(yearly_salaries[0])
# IndexError
# print(yearly_salaries[4])

print(len(yearly_salaries))
print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 3)

yearly_salaries[0] = 100_000
print(yearly_salaries)

yearly_salaries.append(99_999)
print(yearly_salaries)

yearly_salaries.extend([55_000, 66_000])
print(yearly_salaries)

yearly_salaries.insert(1, 111_111)
print(yearly_salaries)

del yearly_salaries[1]
print(yearly_salaries)

yearly_salaries.remove(55_000)
print(yearly_salaries)

yearly_salaries.pop()
print(yearly_salaries)

print(yearly_salaries.count(72_000))

yearly_salaries.sort(reverse=True)
print(yearly_salaries)

yearly_salaries.reverse()
print(yearly_salaries)

texts = ["My", "name", "is", "John", "Doe"]
concated_text = " ".join(texts)
print(concated_text, type(concated_text))

splitted_text = concated_text.split()
print(splitted_text, type(splitted_text))
