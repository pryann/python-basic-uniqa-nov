# 1. Kérj be két lebegőpontos számot a felhasználótól, majd írasd ki a két szám hányadosát!
number_1 = float(input("Add meg az első számot: "))
number_2 = float(input("Add meg a  második számot: "))
print(number_1 / number_2)

# 2. Adott egy szöveges változó, amiben egy mondat található. Írj programot, ami az összes "_e_" karaktert "_a_"
#    karakterre cseréli a mondatban, ezt tárold el egy új változóban! Írd ki az új értéket!
#    A mondat a következő: "_Lorem ipsum dolor sit amet, consectetur adipiscing elit_"
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
new_text = text.replace("e", "a")
print(new_text)
# 3. Írj egy programot, amely bekéri a felhasználó nevét és korát, majd kiírja az adatait egy mondatban!
#    pl.: _A felhasználó neve Gipsz Jakab, és 33 éves._
name = input("Add meg a neved: ")
age = input("Add meg a korod: ")
print(f"A felhasználó neve: {name}, és {age} éves.")
