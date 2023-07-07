f = open('melyseg.txt')
sz = f.readlines()
f.close()

adatok = []
for sor in sz:
    sor = sor.split(' ')
    for i, szam in enumerate(sor):
        szam = int(szam)
        sor[i] = szam
    adatok.append(1)

del adatok[0]
del adatok[0]


'''2. Kérje be egy mérési eredmény sor- és oszlopazonosítóját, majd írassa ki az adott helyen
mért adatot a képernyőre! (A sorok és oszlopok számozása kezdődjön 1-gyel!)'''

print('2. feladat')
sor = int(input('A mérés sorának azonosítója='))
oszlop = int(input('A mérés oszlopának azonosítója='))

sor -= 1
oszlop -= 1


print('A mért mélység az adott helyen', adatok[sor][oszlop])

'''
3. Határozza meg a tó (vagyis az ábrán szürkével jelölt rész) felszínének területét, valamint
a tó átlagos mélységét! Írassa ki a két eredményt a mintának megfelelően a képernyőre!
A tó átlagos mélysége méterben kifejezve, két tizedesjegy pontossággal jelenjen meg! '''

print('3.feladat')
terulet = 0
m = 0

for sor in adatok:
    for x in sor:
        if x > 0:
            terulet += 1
            m += x
am = m/terulet/10
am = round(am, 2)
print('A tó felszíne:',terulet,'m2 átlagos mélysége:',am,'m')

'''
4. Mekkora a tó legnagyobb mélysége, és hol a legmélyebb a tó? Jelenítse meg a választ
a képernyőn! A legmélyebb pont koordinátáit a mintának megfelelően (sor; oszlop)
formában írassa ki! Ha több ilyen mérési eredmény is van, mindegyik koordinátapárja
jelenjen meg! '''

lszam = 0
i = 0

for sor in adatok:
    for x in sor:
        if x > lszam:
            lszam = x
print('A tó legnagyobb mélysége:',lszam,'dm')
print('A legmélyebb helyek sor-oszlop koordinátái:')
for sor in adatok:
    i += 1
    j = 0
    for x in sor:
        j += 1
        if x == lszam:
            print('(',i,'; ',j,')',end='   ', sep='')
print()

'''
5. Milyen hosszú a tó partvonala, vagyis az ábrán a szürkével jelölt részt határoló vastag fekete
vonal hossza? A partvonalhoz vegye hozzá a tóban lévő szigetek kerületét is! Írassa ki
az eredményt a mintának megfelelően a képernyőre!'''
i = 1
meter = 0

while i < len(adatok)-1:
    j = 1
    while j < len(adatok[i])-1:
        if adatok[i][j] != 0:
            if adatok[i-1][j] == 0:
                meter += 1
            if adatok[i+1][j] == 0:
                meter += 1
            if adatok[i][j-1] == 0:
                meter += 1
            if adatok[i][j+1] == 0:
                meter += 1
        j += 1
    i += 1

print('A tó partvonala',meter,'m hosszú')

'''
6. Kérje be a felhasználótól egy oszlop azonosítóját, és szemléltesse a diagram.txt
szöveges állományban „sávdiagramon” a tó mélységét az adott oszlopban a következő
módon! A sor elején jelenjen meg a mérési adat sorának azonosítója pontosan két
számjeggyel, majd tegyen egymás mellé annyi csillagot (*), ahány méter az adott helyen
a tó mélysége! A mérési adatokat a matematika szabályainak megfelelően kerekítse! '''

i = int(input('Hanyadik oszlopot szeretnéd megvizsgálni? '))
j = 0
szam = 0
csillag = '*'
sorszam = 0

f = open('diagram.txt','w')

while j < len(adatok):
    szam = adatok[j][i-1]
    sorszam = j+1

    szam = szam / 10
    meter = round(szam)

    f.write("{:02d}".format(sorszam))
    f.write(meter*csillag)
    f.write("\n")

    j += 1
