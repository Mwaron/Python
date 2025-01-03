print('Ebben a játékban egy kalandor leszel')
print('Egy labirintusban ébredsz és nincs nálad se étel se ital, így az feladatod, hogy kijuss...')
nev=input('Hogyan szólítsalak kedves kalandor? ')
print('Üdvözöllek',nev)
elet=5
ero=3
kijarat = ['b','j','j','j']
lepes = 0
a=0
bentvagy = True
while bentvagy:
    irany = input('Merre induljunk? jobbra vagy balra (j/b) ')
    if kijarat[a]==irany:
        print('Itt frissebb a levegő! Jó irányba haladunk.')
        lepes += 1
        a=a+1
    else:
        print('Elég sötét van itt és mintha valami mozogna az árnyékban..')
        print('A kijárat nem erre van lépjünk vissza egyet…')
    if lepes >= 4:
        bentvagy = False
print('Már látszik a kék ég és a szélben zölden ringatózó fű! Hurrá! Kijutottál!')
