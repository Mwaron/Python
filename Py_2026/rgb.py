"""1. Olvassa be a kep.txt állomány tartalmát, és tárolja el a 640×360 képpont színét!"""

sz = []
with open("kep") as f:
    for line in f:
        line = line.strip().split()
        newLine = []
        i = 0
        while i < len(line):
            newLine.append([int(line[i]), int(line[i+1]), int(line[i+2])])
            t = (int(line[i]), int(line[i+1]), int(line[i+2]))
            i += 3
        sz.append(newLine)

"""2. Kérje be a felhasználótól a kép egy pontjának sor- és oszlopszámát (a számozás mindkét
esetben 1-től indul), és írja a képernyőre az adott képpont RGB színösszetevőit a minta
szerint!"""
print("2. feladat")

#sor = int(input("Sor:"))
#oszlop = int(input("Oszlop:"))
sor = 180
oszlop = 320


"""for i, line in enumerate(sz):
    if i+1 == sor:
        for j, harmasok in enumerate(line):
            if j+1 == oszlop:
                print(f"A képpont színe RGB({harmasok[0]},{harmasok[1]},{harmasok[2]}) ")
                break"""

print(f"A képpont színe RGB({sz[sor-1][oszlop-1][0]},{sz[sor-1][oszlop-1][1]},{sz[sor-1][oszlop-1][2]}) ")


"""3. Világosnak tekintjük az olyan képpontot, amely RGB-értékeinek összege 600-nál nagyobb.
Számolja meg és írja ki, hogy a teljes képen hány világos képpont van! 
"""
print("3. feladat")
db = 0
for line in sz:
    for harmasok in line:
        if sum(harmasok) > 600:
            db += 1

print("A világos képpontok száma:", db)

"""4. A kép legsötétebb pontjainak azokat a pontokat tekintjük, amelyek RGB-értékeinek összege
a legkisebb. Adja meg, hogy mennyi a legkisebb összeg, illetve keresse meg az ilyen RGB
összegű pixeleket, és írja ki mindegyik színét RGB(r,g,b) formában a mintának
megfelelően! """
print("4. feladat")

darkest = []
lOssz = sum(sz[0][0])
for line in sz:
    for harmasok in line:
        if sum(harmasok) < lOssz:
            lOssz = sum(harmasok)

for line in sz:
    for harmasok in line:
        if lOssz == sum(harmasok):
            darkest.append(harmasok)

print("A legsötétebb pont RGB összege:", lOssz)
print("A legsötétebb pixelek színe:")
for harmasok in darkest:
    print(f"RGB({harmasok[0]},{harmasok[1]},{harmasok[2]})")


"""5. Ennek megtalálásához készítsen függvényt hatar néven, amely megadja, hogy egy adott sorban
van-e olyan hely a képen, ahol az egymás melletti képpontok kék színösszetevőinek eltérése
meghalad egy adott értéket! """

def hatar(sor, elteres):
    VoltElteres = False
    for i, harmasok in enumerate(sor[1:]):
        #print(harmasok[-1], sor[i][-1])
        if abs(harmasok[-1] - sor[i][-1]) > elteres:
            VoltElteres = True
    return VoltElteres

"""6. Keresse meg a képen a felhő első és utolsó sorát  az előzőleg elkészített függvény
segítségével úgy, hogy eltérésként 10-et ad meg a függvénynek bemenetként! Adja meg
az első és az utolsó olyan sor sorszámát, ahol az eltérés a soron belül valahol 10-nél
nagyobb! """
print("6. feladat")

elteres = 10
for i, line in enumerate(sz):
    if hatar(line, elteres):
        print("A felhő legfelső sora:",i+1)
        break

for i, line in enumerate(reversed(sz)):
    if hatar(line, elteres):
        print("A felhő legalsó sora:",len(sz)-i)
        break