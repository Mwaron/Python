from datetime import time, datetime

"""1. Olvassa be és tárolja el a további feldolgozáshoz a jeladas.txt állomány tartalmát! """
sz = []
with open("jeladas.txt", "r") as f:
    for line in f:
        line = line.replace("\n", "")
        line = line.split("\t")
        line[-1] = int(line[-1])
        sz.append(line)

"""2. Állapítsa meg, hogy milyen időpontban történt a legutolsó jeladás, és írja a képernyőre
az időpontot, valamint az utoljára jelet adó autó rendszámát! """
print("2. feladat")
print(f"Az utolsó jeladás időpontja {sz[-1][1]}:{sz[-1][2]}, a jármű rendszáma {sz[-1][0]} ")

"""3. Írja ki a bemeneti állományban elsőként szereplő jármű rendszámát, valamint azt, hogy
milyen időpontokban adott jelzést! Az időpontokat óra:perc formátumban, szóközzel
elválasztva, egy sorban jelenítse meg! """
print("3. feladat")

rendsz = sz[0][0]

print(f"Az első jármű: {rendsz} ")
l = []
print("Jeladásainak időpontjai:", end=" ")
for line in sz:
    if line[0] == rendsz:
        print(f"{line[1]}:{line[2]}", end=" ")

print()
"""4. Kérje be a felhasználótól egy időpont óra és perc értékét, és adja meg, hogy hány jeladás
történt az adott időpontban! Ha nem történt jeladás, akkor 0-t írjon ki! 
"""
print("4. feladat")
#ora = input("Kérem, adja meg az órát: ")
#perc = input("Kérem, adja meg a percet: ")
ora = 6
perc = 54
db = 0
for line in sz:
    if line[1] == ora and line[2] == perc:
        db += 1

print("A jeladások száma:", db)
"""5. Állapítsa meg, hogy mennyi az adatok szerint a legnagyobb sebesség, amellyel egy jármű
a jeladáskor haladt, illetve adja meg az összes autó rendszámát, ami haladt ilyen sebességgel! """
print("5. feladat")
speeds = []
for line in sz:
    speeds.append(line[-1])
TopS = max(speeds)
print("A legnagyobb sebesség km/h:", TopS)
print("A járművek:", end=" ")
for line in sz:
    if line[-1] == TopS:
        print(f"{line[0]}", end=" ")
print("")

"""6. Kérje be a felhasználótól egy jármű rendszámát, és jelenítse meg a jármű jeladásainak
időpontját és az adott rendszámú autó távolságát az útszakasz kezdetétől! """
print("6. feladat")


#rendsz = input("Kérem, adja meg a rendszámot:")
rendsz = "ZVJ-638"

l = []
for auto in sz:
    if auto[0] == rendsz:
        l.append(auto)

ossz = 0
print(f"{l[0][1]}:{l[0][2]} 0.0 km")
for i, line in enumerate(l[1:]):
    t1 = int(l[i][1]) * 60 + int(l[i][2])
    t2 = int(l[i+1][1]) * 60 + int(l[i+1][2])
    t = (t2-t1) / 60 * line[-1]
    ossz += t
    print(f"{line[1]}:{line[2]}", round(ossz, 1))

"""7. Készítsen egy ido.txt szöveges állományt, amelynek mindegyik sorában egy-egy jármű
rendszáma, illetve első és utolsó jeladásának óra és perc értéke szerepeljen! Az állományban
minden jármű pontosan egyszer forduljon elő tetszőleges sorrendben! """
print("7. feladat")

mydict = {}
for line in sz:
    if line[0] not in mydict:
        mydict[line[0]] = [f"{line[1]} {line[2]}"]

for line in reversed(sz):
    if len(mydict[line[0]]) == 1:
        mydict[line[0]] += [f"{line[1]} {line[2]}"]

with open("ido.txt", "w") as f:
    for key, value in mydict.items():
        f.write(f"{key} {value[0]} {value[1]}\n")