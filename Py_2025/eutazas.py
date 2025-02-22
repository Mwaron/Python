sz = []
with open("utasadat.txt", 'r') as f:
    for sor in f:
        sor = sor.replace('\n', '')
        sor = sor.split(' ')
        sor[1] = sor[1].split("-")
        sor[1].pop(1)
        sor[1] = int(sor[1][0])
        sor[-1] = int(sor[-1])
        sor[0] = int(sor[0])
        sz.append(sor)

print(sz)
"""2. Adja meg, hogy hány utas szeretett volna felszállni a buszra!"""
print("2. feladat")
print("A buszra",len(sz),"utas akart felszállni. ")

"""3. A közlekedési társaság szeretné, ha a járművőn csak az érvényes jeggyel vagy bérlettel
rendelkezők utaznának. Ezért a jegyeket és bérleteket a buszvezető a felszálláskor ellenőrzi.
(A bérlet még érvényes a lejárat napján.) Adja meg, hogy hány esetben kellett
a buszvezetőnek elutasítania az utas felszállását, mert lejárt a bérlete vagy már nem volt
jegye! """
print('\n3. feladat')
elutasit = 0
for sor in sz:
    if sor[-1] == 0:
        elutasit += 1
    elif sor[-1] < sor[1] and sor[-1] > 100:
        elutasit += 1

print(f"A buszra {elutasit} utas nem szállhatott fel.")

"""4. Adja meg, hogy melyik megállóban próbált meg felszállni a legtöbb utas! (Több azonos
érték esetén a legkisebb sorszámút adja meg!) """
print("\n4.feladat")

lUtas = 0
currentStop = 29
utas = 0
for sor in reversed(sz):
    if sor[0] == currentStop:
        utas += 1
    else:
        if utas >= lUtas:
            lUtas = utas
            thatStop = sor[0]+1
        utas = 1
    currentStop = sor[0]

print(f"A legtöbb utas ({lUtas} fő) a {thatStop}. megállóban próbált felszállni. ")

"""5. A közlekedési társaságnak kimutatást kell készítenie, hogy hányszor utaztak valamilyen
kedvezménnyel a járművön. Határozza meg, hogy hány kedvezményes és hány ingyenes
utazó szállt fel a buszra! (Csak az érvényes bérlettel rendelkező szállhatott fel a buszra!)"""
ingyen = 0
kedvez = 0
ingy = ["NYP", "RVS", "GYK"]
kedv = ['TAB', 'NYB']
for sor in sz:
    if sor[-2] in ingy and sor[-1] >= sor[1]:
        ingyen += 1
    elif sor[-2] in kedv and sor[-1] >= sor[1]:
        kedvez += 1
print(f"Ingyenesen utazók száma: {ingyen} fő")
print(f"A kedvezményes utazók száma: {kedvez} fő")



"""6. Készítsen függvényt napokszama néven az alábbi algoritmus alapján."""
def napokszama(e1, h1, n1, e2, h2, n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2 = 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
    napokszama= d2-d1
    return napokszama

"""7. A közlekedési társaság azoknak az utasoknak, akiknek még érvényes, de 3 napon belül lejár
a bérlete, figyelmeztetést szeretne küldeni e-mailben."""

with open("figyelmeztetes.txt","w") as f:
    for sor in sz:
        if sor[-1] > 100:
            num1 = str(sor[-1])
            num2 = str(sor[1])
            napok = napokszama(int(num2[0:4]), int(num2[4:6]), int(num2[6:]), int(num1[0:4]), int(num1[4:6]), int(num1[6:]))
        if napok <= 3 and napok >= 0:
            f.write(f"{sor[-3]} {num1[0:4]+'-'+num1[4:6]+'-'+num1[6:]}")
            f.write('\n')