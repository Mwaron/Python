"""1. Olvassa be és tárolja el az ut.txt állományban lévő adatokat! """

sz = []
with open('ut', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.replace('\n', '').split(' ')
        line[0] = int(line[0])
        sz.append(line)

sz[0].append("")
print(sz)



"""2. Írja ki az úton található települések nevét! Minden település neve új sorban jelenjen meg!"""
print('2. feladat')
print("A települések neve:")
for line in sz:
    if len(line[1]) >= 4:
        print(line[1])


"""3. Kérjen be a felhasználótól egy valós számot, amely megadja, hogy az út első hány km-es
szakaszát vizsgáljuk! Adja meg, hogy mi volt ezen a szakaszon a legalacsonyabb
sebességhatár! """
print("\n3. feladat")
szakasz = float(input("Adja meg a vizsgált szakasz hosszát km-ben! "))
#szakasz = 1.8
szakasz*=1000
minimum = int(sz[1][1])
CSpeerd = sz[1][1]

for line in sz:
    if line[0] <= szakasz:
        if len(line[1]) == 2 and int(line[1]) < minimum:
            minimum = int(line[1])
        elif len(line[1]) >= 4 and 50 < minimum:
            minimum = 50

print(f"Az első {szakasz/1000} km-en {minimum} km/h volt a legalacsonyabb megengedett sebesség.")

"""4. Adja meg, hogy a bemeneti fájlban rögzített út hány százaléka vezet településen belül! Az út
teljes hossza a bemeneti fájl első sorában található. Az eredményt kéttizedes pontossággal
írja a képernyőre! """
print("\n4. feladat")

def telepulesen(sz):
    num = 0
    kezdes = False
    for line in sz:
        if len(line[1]) >= 4:
            kezdes = line[0]
        elif line[1] == "]":
            vege = line[0]
            num += vege - kezdes
            vege = 0
            kezdes = 0
    return num


print(f"Az út {round(telepulesen(sz)/sz[0][0]*100, 2)} százaléka vezet településen belül.")

""" Olvassa be egy település nevét, és adja meg, hogy a településen belül… hány sebességkorlátozó tábla van; milyen hosszan vezet az út! """
print("\n5. feladat")
telepules = input("Adja meg egy település nevét! ")
#telepules = "Varos010"
kezdes = False
vege = False
t = 0

for line in sz:
    if line[1] == telepules:
        kezdes = True
        KeUt = line[0]
    elif line[1] == "]" and kezdes:
        vege = True
        VeUt = line[0]
        kezdes = False

    if kezdes and not vege:
        num = len(line[1])
        if len(line[1]) == 2:
            t += 1


print(f"A sebességkorlátozó táblák száma: {t}")
print(f"Az út hossza a településen belül {VeUt-KeUt} méter. ")


"""Tavolsagok létrehozása"""
tavolsagok = []
v = False
for line in sz:
    if line[1] == "]":
        vege = line[0]
        v = True
    elif len(line[1]) >= 4:
        koviT = line[0]
        v = False
        tavolsagok.append(koviT - vege)
        tavolsagok.append(line[1])

"""Adja meg a beolvasott településhez legközelebb eső település nevét!"""
print("\n6. feladat")
for i, line in enumerate(tavolsagok):
    if line == telepules:
        telepulesIndex = i
        break

if telepulesIndex == 1:
    print(f"A legközelebbi település: {tavolsagok[telepulesIndex + 2]}")
elif telepulesIndex == len(tavolsagok) - 1:
    print(f"A legközelebbi település: {tavolsagok[telepulesIndex - 2]}")
else:
    if tavolsagok[telepulesIndex-1] >= tavolsagok[telepulesIndex+1]:
        print(f"A legközelebbi település: {tavolsagok[telepulesIndex-2]}")
    else:
        print(f"A legközelebbi település: {tavolsagok[telepulesIndex+2]}")