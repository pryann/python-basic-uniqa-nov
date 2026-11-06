user = {
    "name": "John Doe",
    "age": 33,
    "job": "designer",
    "hobbies": [
        "reading",
        "playing music",
    ],
}

print(user["name"])
print(user["hobbies"])
print(user["hobbies"][0])
user["name"] = "Jane Doe"
print(user)
user["status"] = "dead"
print(user)
user.update({"name": "Kiss Béla", "salary": 100_000})
print(user)
user.pop("salary")
print(user)

print(user.keys())
print(user.values())
print(user.items())

# keys
for k in user:
    print(k)

# values
for v in user.values():
    print(v)

# items
for k, v in user.items():
    print(k, v)
