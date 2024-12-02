f = open('Day2')
sz = f.readlines()
f.close()


def IsItSafe(sor):
    status1 = False
    status2 = False
    inc = sorted(sor)
    dec = sorted(sor, reverse=True)
    if inc == sor or dec == sor:
        status1 = True

    j = 0
    while j < len(sor) - 1:
        n1 = sor[j]
        n2 = sor[j + 1]
        dist = abs(n1 - n2)
        j += 1
        if dist > 0 and dist < 4:
            status2 = True
        else:
            status2 = False
            break

    status = status1 and status2

    return status


i = 0
while i < len(sz):
    line = sz[i]
    sz[i] = line.replace('\n', '')
    i += 1


i = 0
for row in sz:
    sz[i] = row.split(' ')
    i += 1


for row in sz:
    i = 0
    while i < len(row):
        row[i] = int(row[i])
        i += 1




i = 0
safe = 0
while i < len(sz):
    if IsItSafe(sz[i]) == True:
        safe += 1
    else:
        j = 0
        while j < len(sz[i]):
            cp = sz[i].copy()
            cp.pop(j)
            if IsItSafe(cp) == True:
                safe += 1
                break

            j += 1
    i += 1

print(safe)


'''
safe = 0
if IsItSafe(sz) == False:
    i = 0
    j = 0
    while i < len(sz):
        n = sz[i][j]
        sz[i].remove(sz[i][j])

        if IsItSafe(sz):
            safe += 1
        else:
            sz[i].insert(sz[i][j-1], n)
        j += 1
        i += 1
else:
    safe += 1
'''