nev = input("Mi a neved? ")
print("Szia",nev,"!")
print("1. feladat")

n1 = int(input("Mondj egy számot: "))
print(n1*2)
print("2. feladat")

n2 = int(input("Egy másik számot: "))
print("3. feladat")
print(f"az összegük: {n1+n2}, különbségük: {n1-n2}, szorzatuk: {n1*n2}, hányadosuk: {n1/n2}")

"""Ferinek van 236000 Ft-ja, amit befektet kötvényekbe. A befektetés végén Feri a kötvényekért
322140 Ft-ot kap. Írj programot, ami kiszámolja és képernyőre írja, hogy Ferinek hány százalék volt a
hozama (vagyis hány százalékkal nőtt a pénze)! """
print("4. feladat")

fm = 236000
k = 322140
print((k/fm)*100-100,"%", sep='')

"""Béla és Jani állampapírba fektetik a pénzüket. Béla 350000 Ft-ért, Jani 250000 Ft-ért vásárol állampapírt 3 éves futamidővel.
Az állampapír évente fix 7%-ot kamatozik. Írj programot, ami kiszámolja és kiírja képernyőre, hogy a 3 éves futamidő végén mennyi
pénze lesz Bélának és mennyi pénze lesz Janinak! """
print("5. feladat")

B = 350000
J = 250000
k = 1.07
futamido = 3
for i in range(futamido):
    B = B*k
    J = J*k
print(round(B), "Ft")
print(round(J), "Ft")


"""Éva és Marcsi is állampapírt szeretne vásárolni. Írj programot, ahol a program futás közben kell megadni,
hogy Éva mennyi és Marcsi mennyi pénzt szeretne befektetni. Ezeket az összegeket tárold el egy-egy változóba!
Azt is meg lehessen adni, hogy hány évre szeretnék lekötni a pénzüket! A program írja ki, hogy mennyi pénze lesz Évának és
Mennyi pénze lesz Marcsinak a befektetés lejáratakor! A program írja ki azt is, hogy Éva és Marcsi összesen mennyi pénzzel gazdagodtak! """
print("6. feladat")

E = int(input("Eva pénze: "))
M = int(input("Marcsi pénze: "))
befektetes = [E, M]
futamido = int(input("Hány évre szeretnéd befektetni? "))

for i in range(futamido):
    E = E*k
    M = M*k
print(round(E), "Ft, és",round(E-befektetes[0]),"forinttal gazdagodott")
print(round(M), "Ft, és",round(M-befektetes[1]),"forinttal gazdagodott")

"""Írj programot, ami testtömeg indexet számol! A programban a tömeget lehessen megadni kilogrammban, illetve a magasságot
méterben! Nézz utána, hogyan kell ezekből az adatokból kiszámolni a testtömeg indexet és azt alkalmazd a programban!"""
print("7. feladat")

t = int(input("Tömeg: "))
h = float(input("Magasság (m): "))
print(t/(h*h))

"""Készíts programot, amely a burkolásban segít! A burkolandó terület, valamint a csempe szélességét és hosszúságát
megadva a program számolja ki a burkolandó területet, valamint, hogy hány darab csempére van szükség! A csempe számának megadásakor
vegyünk figyelembe 10% ráhagyást, hogy a csempe vágásakor legyen miből dolgoznia a burkolónak! """
print("8. feladat")

s = int(input("Szélesség: "))
h = int(input("Hosszúsağı: "))
print(t*100/(s*h*1.1))

"""Készíts programot, ami útiköltséget számol! A programnak lehessen megadni, hogy hány kilométer távolságot szeretnénk
megtenni, valamint, hogy hány liter üzemanyagot fogyaszt a jármű 100 km-en, továbbá az aktuális üzemanyagárat! A program
írja ki, hogy mennyibe kerül az utazás! 
 """
print("9. feladat")

tavolsag = int(input("Tavolság: "))
uzemanyag = int(input("Uzemanyag: "))
uzemanyag_ar = int(input("Uzemanyag ara: "))


