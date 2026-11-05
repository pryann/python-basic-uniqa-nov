# IMMUTABLE!!!

age = 33
age_copy = age

print(age, id(age))
print(age_copy, id(age_copy))

##############
# 0x000A   33 <----- age
#             <----- age_copy
#############

age = 18
print(age, id(age))
print(age_copy, id(age_copy))

##############
# 0x000A   33   <----- age_copy
#############
# 0x000B   18   <----- age
#############

# MUTABLE
yearly_salaries = [56_000, 72_000, 98_000, 61_000]
yearly_salaries_copy = yearly_salaries
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))
##############
# [56_000, 72_000, 98_000, 61_000]   <----- yearly_salaries
#                                    <----- yearly_salaries_copy
#############
yearly_salaries.append(100_000)
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))
##############
# [56_000, 72_000, 98_000, 61_000, 100_000]   <----- yearly_salaries
#                                             <----- yearly_salaries_copy
#############

# same
yearly_salaries_copy.pop()
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))

# different
yearly_salaries = [1, 2, 3]
print(yearly_salaries, id(yearly_salaries))
print(yearly_salaries_copy, id(yearly_salaries_copy))

# copy  method
yearly_salaries_copy_2 = yearly_salaries.copy()
print(id(yearly_salaries))
print(id(yearly_salaries_copy_2))
