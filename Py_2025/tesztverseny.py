with open('valaszok.txt') as f:
    adatok = {}
    for sor in f:
        sor = sor.replace('\n', '')
        sor = sor.split(' ')
        if 2 != len(sor):
            megoldas = sor[0]
        else:
            adatok[sor[0]] = sor[1]



'''2. Jelenítse meg a képernyőn a mintának megfelelően, hogy hány versenyző vett részt
a tesztversenyen! '''
print('2. feladat:', end=' ')

print(f' A vetélkedőn {len(adatok)} versenyző indult.')




'''3. Kérje be egy versenyző azonosítóját, és jelenítse meg a mintának megfelelően a hozzá
eltárolt válaszokat! Feltételezheti, hogy a fájlban létező azonosítót adnak meg. '''
print('\n3. feladat:', end=' ')

# azon = input('A versenyző azonosítója = ')
azon = 'AB123'

valaszok = adatok[azon]

print(valaszok)


'''4. Írassa ki a képernyőre a helyes megoldást! A helyes megoldás alatti sorba „+” jelet tegyen,
ha az adott feladatot az előző feladatban kiválasztott versenyző eltalálta, egyébként egy
szóközt! A kiírást a mintának megfelelő módon alakítsa ki! 
'''
print('\n4. feladat:')
print(megoldas)


javítás = ''
for i, feladat in enumerate(valaszok):
    if feladat == megoldas[i]:
        javítás += '+'
    else:
        javítás += ' '

print(javítás)


'''5. Kérje be egy feladat sorszámát, majd határozza meg, hogy hány versenyző adott a feladatra
helyes megoldást, és ez a versenyzők hány százaléka! A százalékos eredményt a mintának
megfelelően, két tizedesjeggyel írassa ki! '''
print('\n5. feladat:', end=' ')

# sorszam = input('A feladat sorszáma = ')
sorszam = '10'
sorszam = int(sorszam)


helyes = 0
for feladatok in adatok.values():
    if feladatok[sorszam-1] == megoldas[sorszam-1]:
        helyes += 1

szazalek = helyes/len(adatok)*100

print(f'A feladatra {helyes} fő, a versenyzők {round(szazalek, 2)}%-a adott helyes választ.')



'''6. A verseny feladatai nem egyenlő nehézségűek: az 1-5. feladat 3 pontot, a 6-10. feladat
4 pontot, a 11-13. feladat 5 pontot, míg a 14. feladat 6 pontot ér. Határozza meg az egyes
versenyzők pontszámát, és a listát írassa ki a pontok.txt nevű állományba! Az állomány
minden sora egy versenyző kódját, majd szóközzel elválasztva az általa elért pontszámot
tartalmazza! '''
print('\n6. feladat: A versenyzők pontszámának meghatározása')

def hanypont(feladatok, megoldas):
    pont = 0
    for i, feladat in enumerate(feladatok):
        if feladat == megoldas[i]:
            if 0<=i<=4:
                pont += 3
            elif 5<=i<=9:
                pont += 4
            elif 10<=i<=12:
                pont += 5
            else:
                pont += 6
    return pont


with open('pontok.txt','w') as f:
    for kulcs, ertek in adatok.items():
        pont = hanypont(ertek, megoldas)
        f.write(f'{kulcs} {str(pont)}\n')


'''7. A versenyen a három legmagasabb pontszámot elérő összes versenyzőt díjazzák. Például 5
indulónál előfordulhat, hogy 3 első és 2 második díjat adnak ki. Így megtörténhet az is,
hogy nem kerül sor mindegyik díj kiadására. Írassa ki a mintának megfelelően a képernyőre
a díjazottak kódját és pontszámát pontszám szerint csökkenő sorrendben! '''
print('\n7. feladat: A verseny legjobbjai: ')

pontok = {}

for azon, ertek in adatok.items():
    pont = hanypont(ertek, megoldas)
    if pont not in pontok:
        pontok[pont] = []
    pontok[pont].append(azon)


dobogo = list(set(pontok.keys()))
dobogo.sort(reverse=True)
dobogo = dobogo[0:3]
print(dobogo)

for i, pont in enumerate(dobogo):
    for azon in pontok[pont]:
        print(f'{i+1}. díj ({pont} pont): {azon}')

