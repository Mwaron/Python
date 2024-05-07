#Számokat fog bekérni és kiadni hogy az plaindrom-e vagy nem

szam1 = input("Írj be egy számot: ")
szam2 = input("Írj be egy számot: ")

if szam2 < szam1:
    szam0 = szam1
    szam1 = szam2
    szam2 = szam0

x = 0
while x < len(szam2):
    if szam1[x] in '1234567890' and szam2[x] in '0123456789':
        mérő = True
    else:
        mérő = False
    x += 1


if mérő == True:

    if szam1 == '':
        szam1 = 10
    elif szam2 == '':
        szam2 = 10

    szam1 = int(szam1)
    szam2 = int(szam2)

    psz = szam1
    hatar = int(len(str(psz))/2)

    while psz <= szam2:
        x = 0
        y = -1
        while x <= hatar:
            mérő = False
            if str(psz)[x] == str(psz)[y]:
                x += 1
                y -= 1
                mérő = True
            else:
                break
        if mérő == True:
            print(psz)
        psz +=1
else:
    print('Ez nem egy szám')


