import random
Kártyák = ["Ász","Király","Felső","Alsó","Tizes"]
b = 'i'
while b == 'i':
    i = (random.randint(0,4))
    print(Kártyák[i])
    b = input('Nyomj egy i betűt az ismétléshez: ')
