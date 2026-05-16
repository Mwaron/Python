"""1. Olvassa be és tárolja el a további feldolgozáshoz a jeladas.txt állomány tartalmát! """
sz = []
with open("jeladas.txt","r") as f:
    for line in f:
        line = line.strip().split("\t")
        line[-1] = int(line[-1])
        sz.append(line)

"""2. Állapítsa meg, hogy milyen időpontban történt a legutolsó jeladás, és írja a képernyőre
az időpontot, valamint az utoljára jelet adó autó rendszámát! 
"""
print("2. feladat")
print(f"Az utolsó jeladás időpontja {sz[-1][1]}:{sz[-1][2]}, a jármű rendszáma {sz[-1][0]} ")

"""3. Írja ki a bemeneti állományban elsőként szereplő jármű rendszámát, valamint azt, hogy
milyen időpontokban adott jelzést! Az időpontokat óra:perc formátumban, szóközzel
elválasztva, egy sorban jelenítse meg! 
"""
print("3. feladat")

first = sz[0][0]

print("Az első jármű:", first)
print("Jeladásainak időpontjai: ", end="")
for line in sz:
    if line[0] == first:
        print(f"{line[1]}:{line[2]}", end=" ")
print()
"""4. Kérje be a felhasználótól egy időpont óra és perc értékét, és adja meg, hogy hány jeladás
történt az adott időpontban! Ha nem történt jeladás, akkor 0-t írjon ki! 
"""
print("4. feladat")

#ora = int(input("Kérem, adja meg az órát: "))
#perc = int(input("Kérem, adja meg a percet: "))
ora = 6
perc = 54
db = 0
for line in sz:
    if int(line[1]) == ora:
        if int(line[2]) == perc:
            db += 1

print("A jeladások száma:", db)

"""5. Állapítsa meg, hogy mennyi az adatok szerint a legnagyobb sebesség, amellyel egy jármű
a jeladáskor haladt, illetve adja meg az összes autó rendszámát, ami haladt ilyen sebességgel! """
print("5. feladat")
ln = 0
for line in sz:
    if line[-1] > ln:
        ln = line[-1]

print("A legnagyobb sebesség km/h:", ln)
print("A járművek:", end=" ")
for line in sz:
    if ln == line[-1]:
        print(line[0], end=" ")

print()
"""6. Kérje be a felhasználótól egy jármű rendszámát, és jelenítse meg a jármű jeladásainak
időpontját és az adott rendszámú autó távolságát az útszakasz kezdetétől! """
print("6. feladat")

def atvaltas(ora, perc):
    perc = int(ora)*60+int(perc)
    return perc

#rendszam = input("Kérem, adja meg a rendszámot: ")
rendszam = "ZVJ-638"
auto = []
for line in sz:
    if rendszam == line[0]:
        auto.append(line)


km = 0
print(f"{auto[0][1]}:{auto[0][2]} 0.0 km")
for i, line in enumerate(auto[1:]):
    ido1 = atvaltas(auto[i][1], auto[i][2])
    ido2 = atvaltas(line[1], line[2])
    km += (ido2-ido1)/60*auto[i][-1]
    print(f"{line[1]}:{line[2]} {round(km, 1)} km")


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

with open("ido2.txt", "w") as f:
    for k, v in mydict.items():
        f.write(f"{k} {v[0]} {v[1]}")
        f.write("\n")
