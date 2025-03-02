sz = []
with open("tavirathu13.txt") as f:
    for line in f:
        line = line.replace('\n', '').split(' ')
        line[-1] = int(line[-1])
        line[1] = line[1][:2] + ':' + line[1][2:]
        sz.append(line)

"""2. Kérje be a felhasználótól egy város kódját! Adja meg, hogy az adott városból mikor érkezett
az utolsó mérési adat! A kiírásban az időpontot óó:pp formátumban jelenítse meg! """
print("2. feladat")


print(sz)
kod = input('Adja meg egy település kódját! Település: ')

for line in reversed(sz):
    if line[0] == kod:
        print(f"Az utolsó mérési adat a megadott településről {line[1]}-kor érkezett.")
        break

"""3. Határozza meg, hogy a nap során mikor mérték a legalacsonyabb és a legmagasabb
hőmérsékletet! Jelenítse meg a méréshez kapcsolódó település nevét, az időpontot és
a hőmérsékletet! Amennyiben több legnagyobb vagy legkisebb érték van, akkor elég
az egyiket kiírnia. """
print("\n3. feladat")

maxHo = 0
minHo = 100


for line in sz:
    if line [-1] > maxHo:
        maxHo = line[-1]
        maxvaros = line[0]
        maxIdo = line[1]
    if line[-1] < minHo:
        minHo = line[-1]
        minvaros = line[0]
        minIdo = line[1]

print(f"A legalacsonyabb hőmérséklet: {minvaros} {minIdo} {minHo} fok.")
print(f"A legmagasabb hőmérséklet: {maxvaros} {maxIdo} {maxHo} fok.")

"""4. Határozza meg, azokat a településeket és időpontokat, ahol és amikor a mérések idején
szélcsend volt! (A szélcsendet a táviratban 00000 kóddal jelölik.) Ha nem volt ilyen, akkor
a „Nem volt szélcsend a mérések idején.” szöveget írja ki! A kiírásnál a település kódját és
az időpontot jelenítse meg."""
print("\n4. feladat")

szelcsend = False
for line in sz:
    if line[2] == "00000":
        szelcsend = True
        print(line[0], line[1])

if szelcsend == False:
    print("Nem volt szélcsend a mérések idején.")

"""5. Határozza meg a települések napi középhőmérsékleti adatát és a hőmérséklet-ingadozását!
A kiírásnál a település kódja szerepeljen a sor elején a minta szerint! A kiírásnál csak
a megoldott feladatrészre vonatkozó szöveget és értékeket írja ki! 
"""
print("\n5. feladat")
varosok = ["BP", "DC", "SM", "PA", "SN", "PR", "BC", "PP", "KE"]
idok = ["01", "07", "13", "19"]

for varos in varosok:
    maxHo = 0
    minHo = 100
    kh = 0
    db = 0
    halmaz = set()
    for line in sz:
        if line[-1] > maxHo and line[0] == varos:
            maxHo = line[-1]
        if line[-1] < minHo and line[0] == varos:
            minHo = line[-1]

        if line[0] == varos and line[1][0:2] in idok:
            halmaz.add(line[1][0:2])
            kh += line[-1]
            db += 1


    if len(halmaz) == 4:
        print(f"{varos} középhőmérséklete: {round(kh/db)};  Hőmérséklet-ingadozás: {maxHo - minHo}")
    else:
        print(f"{varos} NA;  Hőmérséklet-ingadozás: {maxHo - minHo}")


"""6. Hozzon létre településenként egy szöveges állományt, amely első sorában a település kódját
tartalmazza! A további sorokban a mérési időpontok és a hozzá tartozó szélerősségek
jelenjenek meg!"""
for varos in varosok:
    with open(varos,"w") as f:
        f.write(f"{varos}\n")
        for line in sz:
            if line[0] == varos:
                f.write(f"{line[1]} ")
                f.write(int(line[2][-2:])*"#")
                f.write('\n')