'''Olvassa be és tárolja el a melyseg.txt fájl tartalmát! Írja ki a képernyőre, hogy az
adatforrás hány adatot tartalmaz! '''
print('1. feladat')

f = open('godor_melyseg.txt', 'r')
szoveg = f.read()
f.close()


adatok = []
adatok = szoveg.split()
i = 0
while i < len(adatok):
    adatok[i] = int(adatok[i])
    i += 1

print('A fájl adatainak száma:', len(adatok))

'''2. Olvasson be egy távolságértéket, majd írja a képernyőre, hogy milyen mélyen van a gödör
alja azon a helyen! Ezt a távolságértéket használja majd a 6. feladat megoldása során is! '''
print('2. feladat')

index = int(input('Adjon meg egy távolságértéket! '))
t = adatok[index-1]
print('Ezen a helyen a felszín',t,'méter mélyen van.')

'''3. Határozza meg, hogy a felszín hány százaléka maradt érintetlen és jelenítse meg 2 tizedes
pontossággal! '''
print('3. feladat')

nullak = 0
for adat in adatok:
    if adat == 0:
        nullak += 1

darabszam = len(adatok)
szazalek = nullak / darabszam * 100
szazalek = round(szazalek, 2)

print('Az érintetlen terület aránya', szazalek)

'''4. Írja ki a godrok.txt fájlba a gödrök leírását, azaz azokat a számsorokat, amelyek egy-egy
gödör méterenkénti mélységét adják meg! Minden gödör leírása külön sorba kerüljön! Az
állomány pontosan a gödrök számával egyező számú sort tartalmazzon! '''
print('4.feldat')


f = open('godor.txt', 'w')
i = 1
while i < len(adatok):
    if adatok[i] != 0:
        f.write(str(adatok[i]))


    elif adatok[i-1] != 0:
        f.write('\n')
    i += 1



'''5. Határozza meg a gödrök számát és írja a képernyőre!'''

print('5. feladat')

godor = 0
i = 1
while i < len(adatok):
    if adatok[i] != 0 and adatok[i-1] == 0:
        godor += 1
    i += 1

print('A gödrök száma:', godor)

'''
6. feladat
a) mi a gödör kezdő és végpontja! A meghatározott értékeket írja a képernyőre!
(Ha nem tudja meghatározni, használja a további részfeladatoknál a 7 és 22
értéket, mint a kezdő és a végpont helyét) '''
print('6. feladat')

def kezdo_pont(index):
    x = 1
    godork = 0
    while adatok[index-1] != 0:
        godork = index
        index -= x
    return godork

def veg_pont(index):
    x = 1
    godorv = 0
    while adatok[index-1] != 0:
        godorv = index
        index += x
    return godorv

print('a)')
kezdopont = kezdo_pont(index)-1
vegpont = veg_pont(index)-1
print('A gödör kezdete:',kezdopont+1,'méter, a gödör vége:',vegpont+1,'méter.')


'''A legmélyebb pontja felé mindkét irányból folyamatosan mélyül-e! Azaz a gödör
az egyik szélétől monoton mélyül egy pontig, és onnantól monoton emelkedik a
másik széléig. Az eredménytől függően írja ki a képernyőr'''
print('b)')

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

legmellyebbIndex = legmellyebbpont(kezdopont, vegpont, adatok)

folyamatos = True
i = kezdopont
while i < legmellyebbIndex:
    if adatok[i] < adatok[i-1]:
        folyamatos = False
        break
    i += 1

i = legmellyebbIndex+1
if folyamatos == True:
    while i < vegpont:
        if adatok[i] < adatok[i+1]:
            folyamatos = False
            break
        i += 1

if folyamatos == True:
    print('Folyamatosan mélyül.')

else:
    print('Nem mélyül folyamatosan.')


'''Mekkora a legnagyobb mélysége! A meghatározott értéket írja a képernyőre! '''
print('c)')

x = kezdopont
legmelyebb = 0
while x <= vegpont:
    if legmelyebb < adatok[x]:
        legmelyebb = adatok[x]
    x += 1
print('A legnagyobb mélység',legmelyebb,'méter.')


'''mekkora a térfogata, ha szélessége minden helyen 10 méternyi! A meghatározott
értéket írja a képernyőre!'''
print('d)')

x = kezdopont
terfogat = 0
while x <= vegpont:
    terfogat += adatok[x]
    x += 1

terfogat = terfogat * 10
print('A térfogata',terfogat,'m^3. ')

'''a félkész csatorna esőben jelentős mennyiségű vizet fogad be. Egy gödör annyi
vizet képes befogadni anélkül, hogy egy nagyobb szélvihar hatására se öntsön
ki, amennyi esetén a víz felszíne legalább 1 méter mélyen van a külső felszínhez
képest. Írja a képernyőre ezt a vízmennyiséget! 
'''
print('e)')

x = kezdopont
vizmennyiseg = 0
while x <= vegpont:
    vizmennyiseg += adatok[x]-1
    x += 1

vizmennyiseg = vizmennyiseg * 10
print('A vízmennyiség',vizmennyiseg,'m^3.')

