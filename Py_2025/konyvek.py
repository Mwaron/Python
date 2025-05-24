"""1. Olvassa be a kiadas.txt vagy a kiadas2.txt bemeneti állományt, és tárolja el annak
tartalmát a memóriában úgy, hogy azokat a későbbi feladatok megoldása során használni
tudja! """
sz = []
with open('kiadas.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.replace('\n', '').split(';')
        line[-1] = int(line[-1])
        line[0] = int(line[0])
        sz.append(line)

"""2. Kérje be a felhasználótól egy szerző nevét, majd adja meg, hány alkalommal adtak ki
a szerzőtől művet az adatok szerint! Amennyiben a szerző neve nem szerepel az adatok
között, úgy a „Nem adtak ki” szöveget jelenítse meg! """
print('2. feladat')

nev = input('Szerző: ')

num = 0
for line in sz:
    if nev in line[3]:
        num += 1

print(num, "könyvkiadás")


"""3. Határozza meg és írja ki, hogy mennyi volt a legnagyobb kiadott példányszám, és ez hány
könyv kiadása esetén fordult elő!"""
print('3. feladat')
max = 0
elofordulas = 1
for line in sz:
    if line[-1] > max:
        max = line[-1]
    elif line[-1] == max:
        elofordulas += 1

print(f"Legnagyobb példányszám: {max}, előfordult {elofordulas} alkalommal ")

"""4. Határozza meg, hogy melyik volt az első olyan külföldi szerzőtől származó mű, amely
legalább 40 000 példányban jelent meg! Tudjuk, hogy volt ilyen könyv. Írja ki a kiadás évét
és negyedévét, valamint a mű leírását a mintának megfelelő formátumban: az évszám után
perjel következzen, a negyedév után pont álljon! """
print('4. feladat')

for line in sz:
    if line[2] == "kf" and line[-1] > 40000:
        print(f"{line[0]}/{line[1]}. {line[3]}")
        break

"""5. Készítsen statisztikát az olyan évekről, amelyekben szerepel, hogy hány alkalommal és
összesen mekkora példányszámban adtak ki magyar, illetve külföldi könyvet! """
print('5. feladat')
print("Év\tMagyar kiadás\tMagyar példányszám\tKülföldi kiadás\tKülföldi példányszám")
date = 2020
while date <= 2023:
    mk = 0
    mp = 0
    kk = 0
    kp = 0
    for line in sz:
        if line[0] == date and line[2] == "ma":
            mk += 1
            mp += line[-1]
        elif line[0] == date and line[2] == "kf":
            kk += 1
            kp += line[-1]
    print(f"{date}\t{mk}\t{mp}\t{kk}\t{kp}")

    date += 1


with open("tabla.html", "w", encoding="UTF-8") as f:
    f.write("<table>\n")
    f.write("<tr><th>Év</th><th>Magyar kiadás</th><th>Magyar példányszám</th><th>Külföldikiadás</th><th>Külföldi példányszám</th></tr> ")
    date = 2020
    while date <= 2023:
        mk = 0
        mp = 0
        kk = 0
        kp = 0
        for line in sz:
            if line[0] == date and line[2] == "ma":
                mk += 1
                mp += line[-1]
            elif line[0] == date and line[2] == "kf":
                kk += 1
                kp += line[-1]
        f.write(f"<tr><td>{date}</td><td>{mk}</td><td>{mp}</td><td>{kk}</td><td>{kp}</td></tr>\n")
        date += 1
    f.write("</table>")

"""6. Szeretnénk tudni, hogy melyek voltak azok a könyvek, amelyeket az első kiadás után még
legalább kétszer, az első kiadásnál nagyobb példányszámban adtak ki újra. Keresse meg a
megfelelő könyveket, és mindegyiket külön sorban jelenítse meg!
"""
print('6. feladat')
print("Legalább kétszer, nagyobb példányszámban újra kiadott könyvek:")

mydict = {}

for line in sz:
    cim = line[3]
    if cim in mydict and line[-1] > mydict[cim][1]:
        mydict[cim][0] += 1
    elif cim not in mydict:
        mydict[cim] = [1, line[-1]]



for key, value in mydict.items():
    if value[0] > 2:
        print(key)