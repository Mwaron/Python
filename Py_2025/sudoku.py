"""1. Olvassa be egy fájl nevét, egy sor és egy oszlop sorszámát (1 és 9 közötti számot)!
A későbbi feladatokat ezen értékek felhasználásával kell megoldania! """
print('1. feladat')

# fajl = input("Adja meg a bemeneti fájl nevét! ")
# sor = int(input("Adja meg a sor számát! "))
# oszlop = int(input("Adja meg az oszlop számát! "))

fajl = 'konnyu.txt'
sor = 1
oszlop = 1
lepesek = []
sz = []
i = 1
with open(fajl, 'r') as f:
    for line in f:
        if i <= 9:
            v = []
            line = line.replace('\n', '').split(' ')
            for num in line:
                num = int(num)
                v.append(num)
            sz.append(v)
            i += 1
        else:
            line = line.replace('\n', '').split(' ')
            lepesek.append(line)

print(lepesek)

"""3. Írja ki a képernyőre, hogy a beolvasott sor és oszlop értékének megfelelő hely…

a. milyen értéket tartalmaz! Ha az adott helyen a 0 olvasható, akkor az „Az adott
helyet még nem töltötték ki.” szöveget jelenítse meg!

b. melyik résztáblázathoz tartozik!"""
print('\n3. feladat')

def resztabla(num):
    if num <= 3:
        return 1
    elif num <= 6:
        return 2
    else:
        return 3


num1 = sz[sor-1][oszlop-1]
if num1 == 0:
    print("Az adott helyet még nem töltötték ki.")
else:
    print(f"Az adott helyen szereplő szám: {num1}")
s = resztabla(sor)
o = resztabla(oszlop)

rtabla = (s-1)*3+o
print(f"A hely a(z) {rtabla} résztáblázathoz tartozik.")


"""4. Határozza meg a táblázat hány százaléka nincs még kitöltve! Az eredményt egy tizedesjegy
pontossággal jelenítse meg a képernyőn! """
print('\n4. feladat')

erintetlen = 0
for sor in sz:
    for num in sor:
        if num == 0:
            erintetlen += 1

print(f"Az üres helyek aránya:  {round(erintetlen/81*100, 1)}%")

"""5. Vizsgálja meg, hogy a fájlban szereplő lépések lehetségesek-e a beolvasott táblázaton! """
print('\n5. feladat')

for lepes in lepesek:
    nemVolt = True
    s = int(lepes[1])
    o = int(lepes[2])
    num = int(lepes[0])

    lsor = resztabla(s)
    loszlop = resztabla(o)
    lRTable = (lsor-1)*3+loszlop

    print(f"\nA kiválasztott sor: {s} oszlop: {o} a szám: {num}")

    if sz[s - 1][o - 1] != 0:
        print("A helyet már kitöltötték")
        nemVolt = False

    if nemVolt:
        for num2 in sz[s - 1]:
            if num2 == num:
                print("Az adott sorban már szerepel a szám")
                nemVolt = False

    if nemVolt:
        for sor in sz:
            if sor[o-1] == num:
                print("Az adott oszlopban már szerepel a szám")
                nemVolt = False

    if nemVolt:
        s2 = 1
        for oszlop in sz:
            o2 = 1
            for num2 in oszlop:

                rs2 = resztabla(s2)
                ro2 = resztabla(o2)
                rTable2 = (rs2 - 1) * 3 + ro2
                if rTable2 == lRTable:
                    if num2 == num:
                        print("A résztáblázatban már szerepel a szám. ")
                        nemVolt = False
                o2 += 1
            s2 += 1


    if nemVolt:
        print("A lepés megtehető.")






