import random

f = open('fejvagyiras')
kiserlet = f.readlines()
f.close()

i = 0
while i < len(kiserlet):
    line = kiserlet[i]
    kiserlet[i] = line.replace('\n', '')
    i += 1

'''1. Szimuláljon egy pénzfeldobást, ahol azonos esélye van a fejnek és az írásnak is!
Az eredményt írassa ki a képernyőre a mintának megfelelően! '''
print('1. feladat')

erme = ["F", "I"]
print(random.choice(erme))

"""2. Kérjen be a felhasználótól egy tippet, majd szimuláljon egy pénzfeldobást! Írassa ki
a képernyőre a felhasználó tippjét és a dobás eredményét is, majd tájékoztassa
a felhasználót az eredményről következő formában: „Ön eltalálta.” vagy „Ön nem
találta el.”! """
print('2. feladat')


"""

tipp = input('Tippeljen! (F/I): ')
if tipp == random.choice(erme):
    print('Ön eltalalta!')
else:
    print('Ön nem talalta el!')

"""

"""3. Állapítsa meg, hány dobásból állt a kísérlet, és a választ a mintának megfelelően írassa ki
a képernyőre! """
print('3. feladat')

print("A kisérelet",len(kiserlet),"dobásból állt!")

"""4. Milyen relatív gyakorisággal dobtunk a kísérlet során fejet? (A fej relatív gyakorisága
a fejet eredményező dobások és az összes dobás hányadosa.) A relatív gyakoriságot
a mintának megfelelően két tizedesjegy pontossággal, százalék formátumban írassa ki
a képernyőre!"""
print('4. feladat')


fej = 0
i = 0
while i < len(kiserlet):
    if kiserlet[i] == "F":
        fej += 1
    i += 1

eredmeny = fej/len(kiserlet)*100
print("A kisérlet során a fej relatív gyakorisága ",round(eredmeny,2),'% volt.', sep='')

"""Hányszor fordult elő ebben a kísérletben, hogy egymás után pontosan két fejet dobtunk?
A választ a mintának megfelelően írassa ki a képernyőre! (Feltételezheti, hogy a kísérlet
legalább 3 dobásból állt.)"""
print('5. feladat')


i = 0
num = 0
while i < len(kiserlet)-1:
    if kiserlet[i] == "F" and kiserlet[i+1] == "F" and kiserlet[i+2] != "F" and kiserlet[i-1] != "F":
        num += 1
    i += 1

print("A kísérlet során",num,"alkalommal dobtak pontosan két fejet egymás után.")

"""Milyen hosszú volt a leghosszabb, csak fejekből álló részsorozat? Írassa ki a választ
a képernyőre a mintának megfelelően, és adja meg egy ilyen részsorozat első tagjának
helyét is! (A minta tagjainak számozását eggyel kezdjük.) """
print('6. feladat')


i = 0
num = 0
maxnum = 0
while i < len(kiserlet):
    if kiserlet[i] == "F":
        num += 1
    else:
        if num > maxnum:
            StartIndex = i - num + 1
            maxnum = num
        num = 0
    i += 1

print("A leghosszabb tisztafej sorozat ",maxnum, " tagból áll, kezdete a(z) " ,StartIndex, ". dobás.", sep='')

"""7. Állítson elő és tároljon a memóriában 1000 db négy dobásból álló sorozatot! Számolja
meg, hogy hány esetben követett egy háromtagú „tisztafej” sorozatot fej, illetve hány
esetben írás! Az eredményt írassa ki a dobasok.txt állományba úgy, hogy az első sorba
kerüljön az eredmény, a második sorban pedig egy-egy szóközzel elválasztva, egyetlen
sorban szerepeljenek a dobássorozatok! """

dobas = []
Rletters = ''
i = 0
while i < 4000:
    Rletters += random.choice(erme)
    if len(Rletters) == 4:
        dobas.append(Rletters)
        Rletters = ''
    i += 1

i = 0
fej = 0
iras = 0
while i < len(dobas):
    if dobas[i] == "FFFF":
        fej += 1
    elif dobas[i] == "FFFI":
        iras += 1
    i += 1

f = open('dobasok.txt','w')

f.write('FFFF: ')
f.write(str(fej))
f.write(", FFFI: ")
f.write(str(iras))
f.write("\n")
for string in dobas:
    f.write(string)
    f.write(" ")

print("The End!")