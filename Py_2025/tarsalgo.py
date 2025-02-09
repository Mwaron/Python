def pbe(o, p):
    p += o * 60
    return p


t = []
l = []
with open('ajto.txt','r') as f:
    for line in f:
        line = line.replace('\n', '')
        line = line.split(' ')
        t.append(pbe(int(line[0]),int(line[1])))
        l.append(line[2:])


'''2. Írja a képernyőre annak a személynek az azonosítóját, aki a vizsgált időszakon belül először
lépett be az ajtón, és azét, aki utoljára távozott a megfigyelési időszakban! '''
print('2. feladat')

print(f"Az első belépő: {l[0][0]}")

i = 600
for sor in reversed(l):
    if sor[1] == 'ki':
        print(f"Az utolsó kilépő: {sor[0]}")
        break

"""3. Határozza meg a fájlban szereplő személyek közül, ki hányszor haladt át a társalgó ajtaján!
A meghatározott értékeket azonosító szerint növekvő sorrendben írja az athaladas.txt
fájlba! Soronként egy személy azonosítója, és tőle egy szóközzel elválasztva az áthaladások
száma szerepeljen! """

dict = {}
with open('athaladas.txt',"w") as f:
    for line in l:
        if line[0] not in dict:
            dict[line[0]] = 1
        else:
            dict[line[0]] += 1

    keys = list(dict.keys())
    i = 0
    while i < len(keys):
        keys[i] = int(keys[i])
        i += 1
    keys.sort()

    for sz in keys:
        f.write(f"{sz} {dict[str(sz)]}\n")

"""4. Írja a képernyőre azon személyek azonosítóját, akik a vizsgált időszak végén a társalgóban
tartózkodtak! """
print("\n4. feladat")

bent = []

for sor in l:
    if sor[1] == "be":
        bent.append(sor[0])
    else:
        bent.remove(sor[0])

for azon in bent:
    print(azon, end=' ')

"""5. Hányan voltak legtöbben egyszerre a társalgóban? Írjon a képernyőre egy olyan időpontot
(óra:perc), amikor a legtöbben voltak bent! """
print('\n\n5. feladat')

max = 0
bent = 0
for i,sor in enumerate(l):
    if sor[1] == "be":
        bent += 1
        if max < bent:
            max = bent
            ido = t[i]
    else:
        bent -= 1


print(f"Például {ido//60}:{ido%60}-kor voltak a legtöbben a társalgóban. ")

"6. Kérje be a felhasználótól egy személy azonosítóját! A további feladatok megoldásánál ezt használja fel! "
azon = input("Adja meg a személy azonosítóját! ")


"""7. Írja a képernyőre, hogy a beolvasott azonosítóhoz tartozó személy mettől meddig
tartózkodott a társalgóban! """
összbent = 0
for i,sor in enumerate(l):
    if azon == sor[0] and sor[1] == "be":
        print(f"{t[i]//60}:{t[i]%60}", end="-")
        összbent += t[i]
        kiment = False
    elif azon == sor[0] and sor[1] == "ki":
        print(f"{t[i]//60}:{t[i]%60}")
        összbent -= t[i]
        kiment = True

print('')

'''8. Határozza meg, hogy a megfigyelt időszakban a beolvasott azonosítójú személy összesen
hány percet töltött a társalgóban!'''
print('\n8. feladat')
if kiment:
    print(f"A(z) {azon}. személy összesen {abs(összbent)} percet volt bent, a megfigyelés végén a társalgóban volt.")
else:
    print(f"A(z) {azon}. személy összesen {abs(összbent-pbe(15, 0))} percet volt bent, a megfigyelés végén a társalgóban volt.")
