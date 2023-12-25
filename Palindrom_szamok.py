#Számokat fog bekérni és kiadni hogy az plaindrom-e vagy nem

szam1 = str(input("Írj be egy számot: "))
szam2 = str(input("Írj be egy számot: "))

x = 0
y = -1
psz = szam1
hatar = int(len(psz)/2)
while x <= hatar:
    mérő = False
    if psz[x] == psz[y]:
        x += 1
        y -= 1
        mérő = True
    else:
        break

print(mérő)
