from itertools import count

from urllib3.packages.six import print_

f = open('Day1')
sz = f.readlines()
f.close()

i = 0
while i < len(sz):
    line = sz[i]
    sz[i] = line.replace('\n', '')
    i += 1


rSide = []
lSide = []

i = 0
for row in sz:
    row = row.split('   ')
    rSide.append(int(row[0]))
    lSide.append(int(row[1]))

rSide = sorted(rSide)
lSide = sorted(lSide)

print(rSide)

i = 0
totalD = 0
while i < len(sz):
    if rSide[i] > lSide[i]:
        totalD += rSide[i] - lSide[i]
    else:
        totalD += lSide[i] - rSide[i]
    i += 1

i = 0
sScore = 0
while i < len(lSide):
    n1 = rSide.count(lSide[i])

    sScore += n1 * lSide[i]

    i += 1

print(sScore)