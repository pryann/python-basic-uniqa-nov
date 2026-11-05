age = 30

# A   B   A and B
# 0   0      0
# 0   1      0
# 1   0      0
# 1   1      1

if age < 18:
    print("Kiskorú")
# elif age >= 18 and age < 65:
elif 18 <= age < 65:
    print("Felnőtt")
else:
    print("Nyugdíjas")


# A   B   A or B
# 0   0      0
# 0   1      1
# 1   0      1
# 1   1      1

prog_lang = "java"
# if prog_lang == "java" or prog_lang == "python":
#     print("backend")

backend_langs = ["java", "python"]
if prog_lang in backend_langs:
    print("backend")

temperature = 50
humidity = 60
rain = True

if temperature > 30 or humidity < 70 and not rain:
    print("Dry weather")
# not rain            False
# humidity < 70       True
#                     False and True  =  False
# temperature > 30    True
#                     False or True   =   True


if (temperature > 30 or humidity < 70) and not rain:
    print("Dry weather")
# temperature > 30    True
# humidity < 70       True
#                     True or True     =  True
# not rain            False
#                     True and False   =  False
