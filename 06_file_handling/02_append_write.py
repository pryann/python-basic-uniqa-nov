# with open("new.txt", "w") as f:
#     f.write("new content")


from os import path

with open("new.txt", "a") as f:
    f.write("\nnew line")

full_path = path.join("06_file_handling", "new.txt")
with open(full_path, "r") as f:
    print(f.read())
