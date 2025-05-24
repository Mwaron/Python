resztvevok=[8654, 9870,6810,8231,9999]

"""Mennyien voltak összesen az 5 koncerten?"""
print("1. Feladat")
ossz = 0
for i in resztvevok:
    ossz += i
print("a) ", ossz)

"""Hány alkalommal voltak többen, mint 8500?"""
ossz = 0
for i in resztvevok:
    if i > 8500:
        ossz += 1

print("\nb)",ossz,"alkalommal")

"""Egy koncertjegy 12500 Ft-ba került. Mennyi bevétel volt az egyes koncerteken?
"""
ossz = 0
print("\nc)")
for i, koncert in enumerate(resztvevok):
    print(f"Az {i+1}. alkalmon {koncert*12500} Ft volt a bevétel")
    ossz += koncert*12500

print("\nd)",ossz)

"""A bevételek 55%-a elment kiadásokra. Mennyi pénz maradt?"""

print("\ne)",ossz*0.55)


print("\n\n2. Feladat")

szamok = [10,20,30,45,22,70,99,50,88,100]

"""A program számolja ki és írja a képernyőre, hogy mennyi a lista elemeinek az összege!"""

print("\n3.")
ossz = 0
for i in szamok:
    ossz += i
print(ossz)


"""A program számolja meg és írja a képernyőre, hogy hány olyan eleme van a listának, ami 50-nél nagyobb!"""

print("\n4.")
ossz = 0
for i in szamok:
    if i > 50:
        ossz += 1

print(ossz)

"""A program írja a képernyőre a lista legnagyobb elemét!"""

print("\n5.")
legnagyobb = 0
for i in szamok:
    if i > legnagyobb:
        legnagyobb = i
print(legnagyobb)


"""A program írja a képernyőre a lista legkisebb elemét!"""
print("\n6.")

legkisebb = 100
for i in szamok:
    if i < legkisebb:
        legkisebb = i
print(legkisebb)


"""A program kérjen be egy számot a felhasználótól és vizsgálja meg, hogy szerepel-e a bekért szám a listában!"""

print("\n7.")
szam = int(input("Adj meg egy számot: "))
if szam in szamok:
    print("Van ilyen szám a listában")
else:
    print("Nincs ilyen szám a listában")


print("\n\nTovábbi feladatok")


peksutemeny = ["kalács", "kifli","kakaóscsiga","kuglóf","kenyér", "kifli","kalács","kifli"]

"""A program írja a képernyőre, hogy hányszor szerepel a kifli a listában!"""

print("\n3.")
ossz = 0
for i in peksutemeny:
    if i == "kifli":
        ossz += 1
print(ossz, "datab")

"""A program kérjen be a felhasználótól egy péksütemény nevet és vizsgálja meg, hogy szerepel-e a
listában a bekért termék! Ha szerepel, akkor írja ki azt is, hogy hányszor!"""

print("\n4.")

sutemeny = input("Adj meg egy péksütemeny nevet: ")

if sutemeny in peksutemeny:
    print("Van ilyen péksütemeny a listában", end=", ")
    ossz = 0
    for i in peksutemeny:
        if i == sutemeny:
            ossz += 1
    print(ossz, "darab.")
else:
    print("Nincs ilyen péksütemeny a listában")



