with open("penztar.txt") as f:
    vasarlasok = []
    vasarlas = []
    for aru in f:
        aru = aru.replace('\n', '')
        if aru != 'F':
            vasarlas.append(aru)
        else:
            vasarlasok.append(vasarlas)
            vasarlas = []


"""2. Határozza meg, hogy hányszor fizettek a pénztárnál!"""
print("\n2. feladat")

print('A fizetések száma:',len(vasarlasok))



'''3. Írja a képernyőre, hogy az első vásárlónak hány darab árucikk volt a kosarában!'''
print('\n3. feladat')

print(f'Az első vásárló {len(vasarlasok[0])} darab árucikket vásárolt.')



'''4. Kérje be a felhasználótól egy vásárlás sorszámát, egy árucikk nevét és egy darabszámot!
A következő három feladat megoldásánál ezeket használja fel!'''
print('\n4. feladat')

"""
sorszam = int(input('Adja meg egy vásárlás sorszámát! '))
aruNev = input('Adja meg egy árucikk nevét! ')
db = int(input('Adja meg a vásárolt darabszámot! '))
"""

sorszam = 2
aruNev = 'kefe'
db = 2

"""5. Határozza meg, hogy a bekért árucikkből
a. melyik vásárláskor vettek először, és melyiknél utoljára!"""
print('\n5. feladat')


elsov = -1
utolsov = -1
darab = 0

for i, vasarlas in enumerate(vasarlasok):
    if aruNev in vasarlas:
        if elsov == -1:
            elsov = i+1

        utolsov = i+1
        darab += 1


print('Az első vásárlás sorszáma:', elsov)
print('Az utolsó vásárlás sorszáma:',utolsov)
print(darab,'vásárlás során vettek belőle.')

"""6. Határozza meg, hogy a bekért darabszámot vásárolva egy termékből mennyi a fizetendő
összeg! A feladat megoldásához készítsen függvényt ertek néven, amely a darabszámhoz
a fizetendő összeget rendeli! """
print('\n6. feladat')

def ertek(mennyiseg):
    osszeg = 0

    if mennyiseg == 1:
        osszeg = 500
    elif mennyiseg == 2:
        osszeg = 950
    elif mennyiseg > 2:
        osszeg = 950 + ((mennyiseg-2)*400)

    return osszeg

print(f'{db} darab vételekor fizetendő: {ertek(db)}')

"""7. Határozza meg, hogy a bekért sorszámú vásárláskor mely árucikkekből és milyen
mennyiségben vásároltak! Az árucikkek nevét tetszőleges sorrendben megjelenítheti."""
print('\n7. feladat')

def tetelek(lista):
    vasarlas = {}
    for aru in lista:
        if aru in vasarlas:
            vasarlas[aru] += 1
        else:
            vasarlas[aru] = 1

    return vasarlas



# vasarlas = {}
# for aru in vasarlasok[sorszam-1]:
#     if aru in vasarlas:
#         vasarlas[aru] += 1
#     else:
#         vasarlas[aru] = 1

vasarlas = tetelek(vasarlasok[sorszam-1])

for aru, db in vasarlas.items():
    print(db, aru)



"""8. Készítse el az osszeg.txt fájlt, amelybe soronként az egy-egy vásárlás alkalmával
fizetendő összeg kerüljön a kimeneti mintának megfelelően! 
"""

with open('osszeg.txt', 'w') as f:
    for i, vasarlas in enumerate(vasarlasok):
        osszeg = 0
        thisDict = tetelek(vasarlas)
        for nev, darab in thisDict.items():
            osszeg += ertek(darab)


        f.write(str(i+1))
        f.write(': ')
        f.write(str(osszeg))
        f.write('\n')



