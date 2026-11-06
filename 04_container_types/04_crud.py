# CRUD: Create Read Update Delete
from venv import create


users = [
    {"id": 1, "first_name": "Una", "last_name": "Gonnet", "email": "ugonnet0@pcworld.com"},
    {"id": 2, "first_name": "Fionna", "last_name": "Fullegar", "email": "ffullegar1@fastcompany.com"},
    {"id": 3, "first_name": "Hussein", "last_name": "Waterhouse", "email": "hwaterhouse2@symantec.com"},
    {"id": 4, "first_name": "Regen", "last_name": "Cantera", "email": "rcantera3@histats.com"},
    {"id": 5, "first_name": "Glenn", "last_name": "Creelman", "email": "gcreelman4@yahoo.co.jp"},
    {"id": 6, "first_name": "Clara", "last_name": "Ashall", "email": "cashall5@europa.eu"},
    {"id": 7, "first_name": "Jarrid", "last_name": "Divers", "email": "jdivers6@tripadvisor.com"},
    {"id": 8, "first_name": "Shea", "last_name": "Thexton", "email": "sthexton7@msu.edu"},
    {"id": 9, "first_name": "Kacie", "last_name": "Glaisner", "email": "kglaisner8@sphinn.com"},
    {"id": 10, "first_name": "Valeda", "last_name": "Yeandel", "email": "vyeandel9@wisc.edu"},
]


def find_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    # return None


print(find_user(4))


def update_user(user_id, payload):
    user = find_user(user_id)
    if user:
        user.update(payload)
        return user


print(update_user(1, {"first_name": "FIRST", "last_name": "LAST"}))


def generate_id():
    return max(user["id"] for user in users) + 1


def create_user(payload):
    # user = {"id": generate_id()}
    # user.update(payload)
    # users.append(user)
    users.append({"id": generate_id(), **payload})
    return users[-1]


print(create_user({"first_name": "Valeda", "last_name": "Yeandel", "email": "vyeandel9@wisc.edu"}))


def remove_user(user_id):
    user = find_user(user_id)
    if user:
        users.remove(user)
        return user


print(remove_user(1))
