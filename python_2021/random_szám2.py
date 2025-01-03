import random
a = random.randint(1,100)
i = 1
print('Gondoltam egy számra 1 és 100 között, megpróbálod kitalálni?')
tipp = 111
while tipp != a:
    tipp = input('Tipp'+str(i)+':')
    tipp=int(tipp)
    i=i+1
    if tipp > a:
        print('A gondolt szám kisebb!')
    elif tipp < a:
        print('A gondolt szám nagyobb!')
    else:
        print('Eltaláltad!')
