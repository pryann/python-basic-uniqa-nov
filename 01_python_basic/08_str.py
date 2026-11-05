# fmt: off
print('banana')
print("banana")
print('I\'m Gergő')
print("\"Cite\"")

print("I'm Gergő")
print('"Cite"')

print("first line\nsecond line")
print("""first line
second line""")

# fmt: on
first_name = "Gergely"
last_name = "Gáll"
age = 42
full_name = first_name + " " + last_name
print(full_name)
print(full_name * 3)

greetings = "My name is " + first_name + ", and I'm " + str(age) + " years old."
print(greetings)
greetings = "My name is {}, and I'm {} years old.".format(first_name, age)
print(greetings)
greetings = "{0}: My name is {0}, and I'm {1} years old.".format(first_name, age)
print(greetings)
greetings = f"My name is {first_name.upper()}, and I'm {age - 10} years old."
print(greetings)

print(len(greetings))
print(greetings[0])
print(greetings[11])
# TypeError: 'str' object does not support item assignment
# str is immutabley
# greetings[0] = "m"

text = "bello"
print(text.capitalize())
print(text.upper())
print(greetings.find("m"))
print(greetings.count("m"))
print(greetings.replace("m", "MMM"))
