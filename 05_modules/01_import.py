# saját modulok
# std lib
# 3.  féltől származó

# modul = python file
# package, csomag = mappa

# import math

# print(math.sin(90))
# print(math.pi)

# from math import pi, sin

# print(pi)
# print(sin(90))

# DO NOT DO THIS!!!
# from math import *

# print(sin(90))
# print(pi)

# module alias
# import math as mathematical

# print(mathematical.sin(90))
# print(mathematical.pi)

# fn alias
from math import cos as cosines
from math import sin as sinus

print(sinus(90))
print(cosines(90))
