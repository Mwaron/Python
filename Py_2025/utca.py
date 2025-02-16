odd = []
even = []
sz = []
with open('kerites.txt') as f:
    for line in f:
        sz.append(line)
        line = line.replace('\n','')
        line = line.split(' ')
        line[1] = int(line[1])
        if line[0] == '0':
            line.pop(0)
            even.append(line)
        else:
            line.pop(0)
            odd.append(line)

"""2. Írja a képernyőre, hogy hány telket adtak el az utcában!"""
print("2. feladat")
print('Az eladott telkek száma: ',len(odd)+len(even))

"""3. Jelenítse meg a képernyőn, hogy az utolsó eladott telek"""
print("\n3. feladat")

if sz[-1][0] == "0":
    print('A páros oldalon adták el az utolsó telket.')
    print('Az utolsó telek házszáma: ', (len(even) - 1) * 2 + 2)

else:
    print('A páratlan oldalon adták el az utolsó telket.')
    print('Az utolsó telek házszáma: ', (len(odd) - 1) * 2 + 1)

"""4. Írjon a képernyőre egy házszámot a páratlan oldalról, amely melletti telken ugyanolyan
színű a kerítés! (A hiányzó és a festetlen kerítésnek nincs színe.) Feltételezheti, hogy van
ilyen telek, a több ilyen közül elég az egyik ház számát megjeleníteni."""
print("\n4. feladat")
color = ""
for i, house in enumerate(odd):
    if color == house[-1] and color != ':' and color != '#':
        print(i*2+1)
        break
    color = house[-1]

"""5. Kérje be a felhasználótól egy eladott telek házszámát, majd azt felhasználva oldja meg a
következő feladatokat!"""
print("\n5.feladat")

num = int(input("Adjon meg egy házszámot! "))

if num%2 == 0:
    i = (num-2)/2
    print('A kerítés szine/állapota: ',even[int(i)][-1])
else:
    i = (num-1)/2
    print('A kerítés szine/állapota: ',odd[int(i)][-1])






"""6. Jelenítse meg az utcakep.txt fájlban a páratlan oldal utcaképét az alábbi mintának
megfelelően!"""
nums = ''
fenc = ""
for i,house in enumerate(odd):
    for vlmi in range(house[0]):
        fenc += house[1]
    nums += str(i*2+1)
    nums += ' '*(house[0]-len(str(i*2+1)))


with open('utcakep.txt','w') as f:
    f.write(fenc)
    f.write("\n")
    f.write(nums)
