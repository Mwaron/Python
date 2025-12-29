"""1. A megadott 15 számot tárolja el a program forrásában egy megfelelő adatszerkezetben!
A 15 szám rendelkezésre áll a tomeg.txt állományban, amelyből a program kódjába
átmásolható. """

l = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]

"""2. A tárgyak tömege alapján határozza meg és írassa ki az össztömeget a minta szerint! """
print("2. feladat")
ossz = 0
for i in l:
    ossz += i

print(f"A tárgyak tömegének összege: {ossz} kg.")

"""3. Határozza meg, hogy hány dobozra van szükség, és ezekben mekkora tömegek lesznek! Az
eredményeket írassa ki a mintának megfelelően! """
print("3. feladat")
ossz = 0
doboz = 0
kgs = ""
for i in l:
    if ossz + i >= 20:
        kgs += str(ossz) + " "
        doboz += 1
        ossz = 0
        ossz += i

    else:
        ossz += i


print(f"A dobozok tartalmának tömege (kg): {kgs}")
print(f"A szükséges dobozok száma: {doboz}")