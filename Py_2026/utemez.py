import datetime
from types import LambdaType

sz = []
with open('taborok.txt') as f:
    for line in f:
        line = line.replace('\n', '')
        line = line.split('\t')
        sz.append(line)


'''2. Jelenítse meg a képernyőn, hogy hány tábor adatait tartalmazza a bemeneti fájl! Írja 
a képernyőre az elsőként és az utolsóként rögzített tábor témáját!'''
print("2. feladat")
print("Az adatsorok száma:",len(sz))
print("Az először rögzített tábor témája:", sz[0][-1])
print("Az utolsóként rögzített tábor témája:",sz[-1][-1])

"""3. Írja a képernyőre, mikor kezdődik a „zenei” tábor! Ha több ilyen tábor is volt, 
az összeset jelenítse meg a lenti mintának megfelelően! Ha egy sem volt, akkor a „Nem 
volt zenei tábor.” szöveget jelenítse meg a képernyőn! """
print("3. feladat")

for line in sz:
    if line[-1] == "zenei":
        print(f'Zenei tábor kezdődik {line[0]}. hó {line[1]}. napján.')

"""4. Keresse meg, melyik táborba jelentkeztek a legtöbben! Írja a képernyőre a tábor kezdő 
dátumát és a témáját! Ha több ilyen tábor is van, az összeset jelenítse meg!"""
print("4. feladat\nLegnépszerűbbek:")
ln = 0
for line in sz:
    if ln < len(line[-2]):
        ln = len(line[-2])

for line in sz:
    if ln == len(line[-2]):
        print(line[0], line[1], line[-1])


"""5. Készítsen függvényt sorszam néven, amely megadja, hogy a paraméterként kapott 
hónap és nap a nyári szünet hányadik napja! """
print('5. feladat')

def sorszam(honap, nap):
    d1 = datetime.datetime(2026, honap, nap)
    szunetkezdes = datetime.datetime(2026, 6, 16)
    return (d1 - szunetkezdes).days + 1

"""6. Kérjen be a felhasználótól egy dátumot a lenti mintának megfelelően, majd adja meg, 
hány tábor zajlik éppen ekkor! 
"""
print("6. feladat")

ho = int(input("hó: "))
nap = int(input("nap: "))
jelennap = sorszam(ho, nap)
db = 0
for line in sz:
    tkezdes = sorszam(int(line[0]), int(line[1]))
    tveg = sorszam(int(line[2]), int(line[3]))
    if tkezdes <= jelennap <= tveg:
        db += 1

print(f"Ekkor éppen {db} tábor tart.")

"""7. Olvassa be egy tanuló betűjelét! Határozza meg, hogy az adott betűjelű tanuló mely 
táborok iránt érdeklődött!"""
print("7. feladat")

rendezes = []
betu = input("Adja meg egy tanuló betűjelét: ")
with open("egytanulo.txt", "w") as f:
    for line in sz:
        if betu in line[-2]:
            rendezes.append([int(line[0]), int(line[1]), int(line[2]), int(line[3]), line[-1]])

    rendezes.sort()
    for line in rendezes:
        f.write(f"{line[0]}.{line[1]}-{line[2]}.{line[3]}. {line[-1]}\n")


OK = True
for i ,line in enumerate(rendezes[:-1]):
    if datetime.datetime(2026, line[2], line[3]) > datetime.datetime(2026, rendezes[i+1][0], rendezes[i+1][1]):
        OK = False
        print("Nem mehet el mindegyik táborba.")
        break

if OK:
    print("Elmehet mindegyik táborba.")