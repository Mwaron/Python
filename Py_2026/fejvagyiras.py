import random
erme = ["F", "I"]
"""print('1. feladat')

print(f"A pénzfeldobás eredménye: {random.choice(erme)}")

print("2. feladat")
tipp = input("Tippeljen! (F/I)= ")
ran = random.choice(erme)
print(f"A tipp {tipp} volt, a dobás eredménye {ran} volt.")
if tipp == ran:
    print("Ön eltalálta.")
else:
    print("Ön nem találta el.")
"""
"""1. Szimuláljon egy pénzfeldobást, ahol azonos esélye van a fejnek és az írásnak is!
Az eredményt írassa ki a képernyőre a mintának megfelelően!"""

"""3. Állapítsa meg, hány dobásból állt a kísérlet, és a választ a mintának megfelelően írassa ki
a képernyőre!"""
print("3. feladat")
fej = 0
iras = 0
with open('kiserlet.txt', encoding='utf-8') as f:
    for i, s in enumerate(f):
        #4. feladat része
        if s == 'F\n':
            fej += 1
        else:
            iras += 1
    print(f"A kisérlet {i+1} dobásból állt.")

"""4. Milyen relatív gyakorisággal dobtunk a kísérlet során fejet? (A fej relatív gyakorisága
a fejet eredményező dobások és az összes dobás hányadosa.) A relatív gyakoriságot
a mintának megfelelően két tizedesjegy pontossággal, százalék formátumban írassa ki
a képernyőre! """
print("4. feladat")
print(f"A fej relatív gyakorisága: {fej / (fej + iras) * 100:.2f}%")

"""5. Hányszor fordult elő ebben a kísérletben, hogy egymás után pontosan két fejet dobtunk?"""
print("5. feladat")
num = 0
l = []
lIndex = []
with open('kiserlet.txt', encoding='utf-8') as f:
    for i, s in enumerate(f):
        if s == 'F\n':
            num += 1
        else:
            l.append(num)
            num = 0

print(f'A kisérlet során {l.count(2)} alkalommal dobtak pontosan két fejet egymás után.')

"""6. Milyen hosszú volt a leghosszabb, csak fejekből álló részsorozat?"""
print("6. feladat")

with open('kiserlet.txt', encoding='utf-8') as f:
    tarolo = []
    max_l = 0
    max_i = 0
    for i, s in enumerate(f):
        if s == 'F\n':
            tarolo.append(i)
        else:
            if len(tarolo) > max_l:
                max_l = len(tarolo)
                max_i = tarolo[0]
            tarolo = []
    print(f"A leghosszabb,tisztafej sorozat {max_l} tagböl assh, kezdete a(z). {max_i+1} dobás.")

"""7. Állítson elő és tároljon a memóriában 1000 db négy dobásból álló sorozatot! """

dobasok = []
string = ''
for i in range(4000):
    string += random.choice(erme)
    if len(string) == 4:
        dobasok.append(string)
        string = ''

with open('dobasok.txt', 'w', encoding='utf-8') as f:
    f.write(f"FFFF: {dobasok.count('FFFF')}, FFFI: {dobasok.count('FFFI')}")
    f.write("\n")
    for s in dobasok:
        f.write(s)
        f.write(" ")