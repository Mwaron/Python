date = []
hianyzok = []
with open(' naplo.txt', 'r') as f:
    for sor in f:
        if sor[0] == '#':
            date.append(sor.replace('\n', ''))
            l = []
            hianyzok.append(l)

        else:
            l.append(sor.replace('\n', ''))

'''2. Határozza meg és írassa ki, hogy hány sor van a fájlban, ami hiányzást rögzít! (A fenti
példában 3 ilyen bejegyzés van.) '''
print('2. feladat ')
db = 0
for sor in hianyzok:
    db += len(sor)

print(f'A naplóban {db} bejegyzés van. ')

'''3. Számolja meg és írassa ki, hogy összesen hány óra igazolt és hány óra igazolatlan hiányzás
volt a félév során!'''
print('\n3. feladat')

igazolt = 0
igazolatlan = 0
for nap in hianyzok:
    for diak in nap:
        orak = diak[-7:]
        for ora in orak:
            if ora == "X":
                igazolt += 1
            elif ora == "I":
                igazolatlan += 1

print(f'Az igazolt hiányzások száma {igazolt}, az igazolatlanoké {igazolatlan} óra.')

"4. feladat"


def hetnapja(honap: int, nap: int) -> str:
    napnev = ("vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat")
    napszam = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335)
    napsorszam = (napszam[honap - 1] + nap) % 7
    return napnev[napsorszam]


'''5. Kérjen be egy dátumot (hónap, nap), és a hetnapja függvény felhasználásával írassa ki,
hogy az a hét melyik napjára esett! '''
print('\n5. feladat')

honap = int(input('A hónap sorszáma: '))
nap = int(input('A nap sorszáma: '))

print(f'Azon a napon {hetnapja(honap, nap)} volt.')


'''6. Kérje be a hét egy tanítási napjának nevét és egy aznapi tanítási óra óraszámát (például:
kedd 3)! Írassa ki a képernyőre, hogy a félév során az adott tanítási órára összesen hány
hiányzás jutott!'''
print('\n6. feladat')

napnev = input('A nap neve: ')
ora = int(input('Az óra sorszáma: ')) - 1
hianyzas = 0

for i, nap in enumerate(date):
    if hetnapja(int(nap[2:4]), int(nap[5:7])) == napnev:
        for diak in hianyzok[i]:
            orak = diak[-7:]
            if orak[ora] == 'X' or orak[ora] == 'I':
                hianyzas += 1

print(f'Ekkor összesen {hianyzas} óra hiányzás történt.')

'''7. Írassa ki a képernyőre a legtöbb órát hiányzó tanuló nevét! Ha több ilyen tanuló is van,
akkor valamennyi neve jelenjen meg szóközzel elválasztva! '''
print('\n7. feladat\nA legtöbbet hiányzó tanulók: ', end='')
hianyzas = {}

for diakok in hianyzok:
    for diak in diakok:
        nev = diak[0:-8]
        orak = diak[-7:]

        szam = orak.count('I') + orak.count('X')  # TODO megtanulni

        if nev not in hianyzas:
            hianyzas[nev] = 0
        else:
            hianyzas[nev] += szam

max = 0
for ertek in hianyzas.values():
    if max < ertek:
        max = ertek

for kulcs, ertek in hianyzas.items():
    if ertek == max:
        print(kulcs, end=' ')
