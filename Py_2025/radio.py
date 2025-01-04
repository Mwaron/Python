l1 = []
l2 = []
with open("vetel.txt") as f:
    for i, line in enumerate(f):
        if i % 2 == 0:
            l1.append(line.replace('\n','').split(" "))

        else:
            l2.append(line.replace('\n',''))


def szame(szo:str) -> bool:
    valasz = True
    for i in range(len(szo)):
        if szo[i]<'0' or szo[i]>'9':
            valasz = False

    return valasz



def merge(lst:list) -> str:
    result = ''

    for k in range(len(lst[0])):
        ch = "#"
        for i, line in enumerate(lst):
            if lst[i][k] != "#":
                ch = lst[i][k]
                break
        result += ch

    return result







"""2. Írja a képernyőre, hogy melyik rádióamatőr rögzítette az állományban szereplő első és
melyik az utolsó üzenetet! """
print("2. feladat")

print('Az első üzenet rögzítője:',l1[0][1])
print('Az utolsó üzenet rögzítője:',l1[-1][1])

"""3. Adja meg az összes olyan feljegyzés napját és a rádióamatőr sorszámát, amelynek
szövegében a „farkas” karaktersorozat szerepel! """
print("\n3. feladat")

for i, line in enumerate(l2):
    if "farkas" in line:
        print(l1[i][0],'. nap ',l1[i][1],'. rádióamatőr ', sep='')

        # print(f"{l1[i][0]}. nap {l1[i][1]}. rádióamatőr ")

"""4. Készítsen statisztikát, amely megadja, hogy melyik napon hány rádióamatőr készített
feljegyzést. Azok a napok 0 értékkel szerepeljenek, amikor nem született feljegyzés!
Az eredmény a képernyőn jelenjen meg a napok sorszáma szerint növekvően!
A megjelenítést a feladat végén látható minta szerint alakítsa ki! """
print('\n4. feladat')

day = 1
i = 0
while day <= 11:
    num = 0
    for line in l1:
        if line[0] == str(day):
            num += 1
    print(f"{day}. nap: {num} rádióamatőr ")
    day += 1

"""5. A rögzített üzenetek alapján kísérelje meg helyreállítani az expedíció által küldött
üzenetet! Készítse el az adaas.txt fájlt, amely napok szerinti sorrendben tartalmazza
a küldött üzeneteket! Ha egy időpontban senkinél nem volt vétel, akkor azon a ponton a #
jel szerepeljen! (Feltételezheti, hogy az azonos üzenethez tartozó feljegyzések között
nincs ellentmondás.)"""

with open('addaas.txt','w') as f:
    for day in range(1,12):
        l3 = []
        for i, line in enumerate(l1):
            if line[0] == str(day):
                l3.append(l2[i])
        s = merge(l3)
        f.write(s)
        f.write('\n')


'''7. Olvassa be egy nap és egy rádióamatőr sorszámát, majd írja a képernyőre a megfigyelt
egyedek számát (a kifejlett és kölyök egyedek számának összegét)! Ha nem volt ilyen
feljegyzés, a „Nincs ilyen feljegyzés” szöveget jelenítse meg! Ha nem volt megfigyelt
egyed vagy számuk nem állapítható meg, a „Nincs információ” szöveget jelenítse meg!
Amennyiben egy számo'''