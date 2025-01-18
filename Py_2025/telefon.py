'''1. Készítse el az mpbe függvényt, amely az óra, perc, másodperc alakban megadott időpont
másodpercben kifejezett értékét adja! A függvényt a megoldásba be kell építenie!'''

def mpbe(o, p, mp):
    mp = mp
    mp += o*60*60
    mp += p*60
    return mp

hk = []
hv = []



with open("hivas.txt") as f:
    for sor in f:
        sor = sor.replace('\n', '')
        sor = sor.split(' ')

        for i, num in enumerate(sor):
            sor[i] = int(num)

        hk.append(sor[0:3])
        hv.append(sor[3:6])

bk = [[0, 0, 0]]
temp = 0
for i, ido in enumerate(hk):
    if hv[i][0] == 6 or hk[i][0] >= 12:
        bk.append([0, 0, 0])
    else:
        if temp < mpbe(hv[i][0], hv[i][1], hv[i][2]):
            bk.append(hv[i])
            temp = mpbe(hv[i][0], hv[i][1], hv[i][2])
        else:
            bk.append([0, 0, 0])

print(bk)



"""3. Készítsen statisztikát, amely megadja, hogy óránként hány hívás futott be! A képernyőn
soronként egy óra-darabszám párost jelenítsen meg! Csak azok az órák jelenjenek meg,
amelyben volt hívás!"""
print('3. feladat')

i = 0
thisdict = {}
for sor in hk:
    if sor[0] in thisdict:
        thisdict[sor[0]] += 1
    else:
        thisdict[sor[0]] = 1

for ora, num in thisdict.items():
    print(ora,'ora', num,'hivas')

"""4. Írja a képernyőre a leghosszabb hívásnak a sorszámát és másodpercben kifejezett hosszát –
attól függetlenül, hogy a hívó tudott-e beszélni az ügyfélszolgálatossal vagy sem! Azonos
híváshossz esetén elegendő egyet megjelenítenie."""
print('\n 4. feladat')

h1 = 0
for i,l in enumerate(hk):
    h2 = mpbe(hv[i][0],hv[i][1],hv[i][2])-mpbe(l[0],l[1],l[2])
    if h2 > h1:
        k = i
        h1 = h2

print(f'A leghosszabb ideig vonalban levo hivo {k+1}. sorban szerepel, a hivas hossza: {h1} masodperc.')



'''5. Olvasson be egy munkaidőn belüli időpontot, majd jelenítse meg a képernyőn, hogy
hanyadik hívóval beszélt akkor az alkalmazott, és éppen hányan vártak arra, hogy sorra
kerüljenek! Ha nem volt hívó, akkor a „Nem volt beszélő.” üzenetet jelenítse meg!'''
print('\n 5. feladat')


'''ido = input('Adjon meg egy idopontot! (ora perc masodperc) ')'''
ido = '10 11 12'

print('Hívás kezdete:',hk[-1])
print('Hívás vége:',hv[-1])
print('Beszélgetés kezdete:',bk[-1])