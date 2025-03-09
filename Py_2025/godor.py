"""1. Olvassa be és tárolja el a melyseg.txt fájl tartalmát! Írja ki a képernyőre, hogy az
adatforrás hány adatot tartalmaz!
"""
sz = []
print('1. feladat')
with open('melyseg.txt', 'r') as f:
    for line in f:
        sz.append(int(line.replace('\n', '')))


print(f"A fájl adatainak száma: {len(sz)}")

"""2. Olvasson be egy távolságértéket, majd írja a képernyőre, hogy milyen mélyen van a gödör alja azon a helyen!
Ezt a távolságértéket használja majd a 6. feladat megoldása során is! """
print('\n2. feladat')

index = int(input('Adjon meg egy távolságértéket! '))
print(f"Ezen a helyen a felszín {sz[index-1]} méter mélyen van.")

"""3. Határozza meg, hogy a felszín hány százaléka maradt érintetlen és jelenítse meg 2 tizedes
pontossággal! """
print('\n3. feladat')

erintetlen = 0
for melyseg in sz:
    if melyseg == 0:
        erintetlen += 1

print(f"Az érintetlen terület aránya {round(erintetlen/len(sz)*100, 2)}%")

"""4. Írja ki a godrok.txt fájlba a gödrök leírását, azaz azokat a számsorokat, amelyek egy-egy
gödör méterenkénti mélységét adják meg! Minden gödör leírása külön sorba kerüljön! Az
állomány pontosan a gödrök számával egyező számú sort tartalmazzon! 
"""
godor = ""
godrok = 0
with open("godrok.txt", 'w') as f:
    for line in sz:
        if line != 0:
            godor += str(line) + ' '
        else:
            if godor != "":
                f.write(f"{godor}\n")
                godrok += 1
                godor = ""

"""5. Határozza meg a gödrök számát és írja a képernyőre!"""
print('\n5. feladat')

print(f"A gödrök száma: {godrok}")


"""6. Ha a 2. feladatban beolvasott helyen nincs gödör, akkor „Az adott helyen nincs gödör.”
üzenetet jelenítse meg, ha ott gödör található, akkor határozza meg, hogy """
print('\n6. feladat')

"""a) mi a gödör kezdő és végpontja! A meghatározott értékeket írja a képernyőre!
(Ha nem tudja meghatározni, használja a további részfeladatoknál a 7 és 22
értéket, mint a kezdő és a végpont helyét) """


volt = False
j = 0
if sz[index-1] == 0:
    print('Az adott helyen nincs gödör.')
else:
    print('a)')
    for i, line in enumerate(reversed(sz[:index])):
        if line == 0 and volt == False:
            j = i - 1
            volt = True

    for k, line in enumerate(sz):
        if line == 0 and index < k:
            break
kpont = i - j + 1
vpont = k

print(f"A gödör kezdete: {kpont} méter, a gödör vége: {vpont} méter.")


"""b) a legmélyebb pontja felé mindkét irányból folyamatosan mélyül-e! Azaz a gödör
az egyik szélétől monoton mélyül egy pontig, és onnantól monoton emelkedik a
másik széléig. Az eredménytől függően írja ki a képernyőre a „Nem mélyül
folyamatosan.” vagy a „Folyamatosan mélyül.” mondatot! """
print("b)")

def legmellyebbpont(kp, vp, adatok):
    maxIndex = 0
    maxErtek = 0
    i = kp
    while i <= vp:
        if adatok[i] > maxErtek:
            maxIndex = i
            maxErtek = adatok[i]
        i += 1
    return maxIndex

legmellyebbIndex = legmellyebbpont(kpont, vpont, sz)

folyamatos = True
i = kpont
while i < legmellyebbIndex:
    if sz[i] < sz[i-1]:
        folyamatos = False
        break
    i += 1

i = legmellyebbIndex+1
if folyamatos == True:
    while i < vpont:
        if sz[i] < sz[i+1]:
            folyamatos = False
            break
        i += 1

if folyamatos == True:
    print('Folyamatosan mélyül.')

else:
    print('Nem mélyül folyamatosan.')



"""c) Mekkora a legnagyobb mélysége! A meghatározott értéket írja a képernyőre! """
print("c)")
maxM = 0
for i, line in enumerate(sz):
    if i <= vpont and i >= kpont and line > maxM:
        maxM = line

print(f"A legnagyobb mélysége {maxM} méter. ")

"""d) mekkora a térfogata, ha szélessége minden helyen 10 méternyi! A meghatározott
értéket írja a képernyőre! """
print("d)")
terfogat = 0
for i, line in enumerate(sz):
    if i >= kpont-1 and i <= vpont:
        terfogat += line

print(f"A térfogat: {terfogat*10} m^3.")

"""e) a félkész csatorna esőben jelentős mennyiségű vizet fogad be. Egy gödör annyi
vizet képes befogadni anélkül, hogy egy nagyobb szélvihar hatására se öntsön
ki, amennyi esetén a víz felszíne legalább 1 méter mélyen van a külső felszínhez
képest. Írja a képernyőre ezt a vízmennyiséget! """
print("e)")
vmenny = 0
for i, line in enumerate(sz):
    if i >= kpont-1 and i <= vpont and line > 1:
        vmenny += 1

print(f"A vízmennyiség {terfogat*10-(vpont-kpont+1)*10} m^3.")