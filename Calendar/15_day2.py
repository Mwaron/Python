f = open('15_day2')
sz = f.readlines()
f.close()


i = 0

while i < len(sz):
    j = 0
    sz[i] = sz[i].split('x')
    while j < 3:
        sz[i][j] = int(sz[i][j])
        j += 1
    i += 1

szam = 0
szalag = 0

for e in sz:
    if e[0] > e[1]:
        e[0], e[1] = e[1], e[0]

    if e[0] > e[2]:
        e[0], e[2] = e[2], e[0]

    if e[1] > e[2]:
        e[1], e[2] = e[2], e[1]

    sq = 2*e[0]*e[1]+2*e[0]*e[2]+2*e[1]*e[2]
    sq += e[0]*e[1]
    szam += sq
    szalag += e[0] + e[0] + e[1] + e[1] + e[0]*e[1]*e[2]

print(szam)
print(szalag)
