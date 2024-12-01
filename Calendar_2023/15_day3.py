f = open('15_day3')
sz = f.read()
f.close()


h = [0, 0]
Rh = [0, 0]

adatok = [h]
adatok2 = [Rh]

def move(h, way):
    h2 = [h[0], h[1]]
    if way =="^":
        h2[1] += 1
    elif way =="v":
        h2[1] -= 1
    elif way ==">":
        h2[0] += 1
    else:
        h2[0] -= 1

    return h2

i = 0
while i < len(sz):
    way = sz[i]
#Sima Santa
    if i % 2 == 0:
        way = sz[i]
        h = move(h, way)
        if h not in adatok:
            adatok.append(h)

#Robot Santa
    if i % 2 != 0:
        way = sz[i]
        Rh = move(Rh, way)
        if Rh not in adatok:
            adatok2.append(Rh)

    i += 1

i = 0
while i < len(adatok2):
    if adatok2[i] not in adatok:
        adatok.append(adatok2[i])
    i += 1

print(len(adatok))

