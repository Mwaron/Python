import random
k='i'
while k=='i':
    a= random.randint(1,6)
    b= random.randint(1,6)
    print('Az első játékos dobásának összege: ',a+b)
    c= random.randint(1,6)
    d= random.randint(1,6)
    print('A második játékos dobásának összege:',c+d)
    if a+b>c+d:
        print('Az első játékos nyert!')
    elif a+b<c+d:
        print('A második játékos nyert!')
    else:
        print('Döntetlen!')
    k=input('nyomj egy i betűt ha szeretnéd újra kezdeni: ')
