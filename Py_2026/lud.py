o = []
with open("osvenyek.txt", "r") as f:
    for line in f:
        line = line.replace("\n", "")
        o.append(line)

d = []
dob = []
with open("dobasok.txt", "r") as f:
    d=f.read().split(" ")
    for s in d:
        dob.append(int(s))

"""2. Jelenítse meg a képernyőn, hogy hány ösvény adatait tartalmazza az osvenyek.txt fájl,
és mennyi dobás szerepel a dobasok.txt fájlban! """
print("2. feladat")
print("A dobások száma:", len(dob))
print("Az ösvények száma:", len(o))

"""3. Határozza meg, hogy melyik ösvény áll a legtöbb mezőből, és jelenítse meg az ösvény
sorszámát és a mezők számát! Ha több ilyen is van, elegendő egyet megjelenítenie. """
print("3. feladat")

legn = 0
legni = 0
for i, line in enumerate(o):
    if legn < len(line):
        legn = len(line)
        legni = i

print(f"Az egyik leghosszabb a(z) {legni+1}. ösvény, hossza: {legn} ")

"""4. Olvassa be és tárolja el egy ösvény sorszámát és a játékot játszók számát (legalább 2,
legfeljebb 5)! A későbbiekben ezekkel az adatokkal dolgozzon! """
print("4. feladat")
osvSzam = int(input("Adja meg egy ösvény sorszámát! "))
jatSzam = int(input("Adja meg a játékosok számát! "))


"""5. Készítsen statisztikát a megadott sorszámú ösvény mezőiből! Jelenítse meg, hogy ez milyen
típusú mezőből mennyit tartalmaz!"""
print("5. feladat")
M = 0
V = 0
E = 0
for s in o[osvSzam-1]:
    if s == "M":
        M += 1
    elif s == "V":
        V += 1
    elif s == "E":
        E += 1

if M != 0:
    print("M:", M)
if V != 0:
    print("V:", V)
if E != 0:
    print("E:", E)

"""6. Írja a kulonleges.txt fájlba, hogy a választott ösvény mely mezői különlegesek!
Soronként egy mezőt adjon meg a mező sorszámával és a mező típusát megadó karakterrel!
A két értéket egy tabulátor karakterrel válassza el egymástól! """
l = []
for i, s in enumerate(o[osvSzam-1]):
    if s == "V" or s == "E":
        l.append(f"{i+1}\t{s}")

with open("kulonleges.txt", "w") as f:
    for line in l:
        f.write(line)
        f.write("\n")

"""7. Határozza meg, hogy melyik játékos jutna a legmesszebb, ha a választott ösvényen minden
mező M típusú lenne! """
print("7. Feladat")
jatekosok = []
for i in range(jatSzam):
    jatekosok.append(0)

ossz = 0
i = 0
for num in dob:
    jatekosok[i] += num
    if jatekosok[i] >= len(o[osvSzam-1]):
        break
    else:
        if i >= jatSzam-1:
            i = 0
            ossz += 1
        else:
            i += 1

legn = 0
for i, s in enumerate(jatekosok):
    if legn < s:
        legni = i

print(f"A játék a(z) {ossz+1}. körben fejeződött be. A legtávolabb jutó(k) sorszáma: {legni+1}")

"""8. Határozza meg, ki nyer, ha figyelembe veszi a mezők típusát is! Jelenítse meg a nyertes(ek)
sorszámát és azt, hogy a többi bábu milyen sorszámú mezőn áll az utolsó teljes kör végén!"""
print("8. Feladat")
jatekosok = []
for i in range(jatSzam):
    jatekosok.append(0)

nyert = []
osveny = o[osvSzam-1]
i = 0
megy = True
kor = 1

for num in dob:
    if megy:
        #currentBlock = osveny[jatekosok[i]+num-1]
        ujpoz = jatekosok[i]+num

        if ujpoz >= len(osveny)-1:
            nyert.append(i+1)
            jatekosok[i] += num
        elif osveny[ujpoz-1] == "M":
            jatekosok[i] += num
        elif osveny[ujpoz-1] == "E":
            jatekosok[i] += 2*num
            if jatekosok[i] >= len(osveny)-1:
                nyert.append(i+1)

        if i >= jatSzam-1:
            i = 0
            kor += 1
            if nyert != []:
                megy = False
        else:
            i += 1
    else:
        break

print("Nyertes(ek):",*nyert)
for i, mezo in enumerate(jatekosok):
    if i+1 not in nyert:
        print(f"{i+1}. játékos, {mezo}. mező")



