import random
print('A nyertes lottó számok!')
szamok = []
i=1
while i <= 5:
    a = random.randint(1,90)
    benne = False
    j = 0
    while j < len(szamok):
        if a == szamok[j]:
            benne = True
        j=j+1    

    if benne == False:
        szamok.append(a)
        i=i+1
print(szamok)
    
