összes=[]
Vege=1
Dobas=1
a=0
b=0
print('Elég csak a rövidítésüket kiírni pl: Fej=F')
while Vege!='':
    Dobas = input('Most mit dobtál? ')
    if Dobas == 'F':
        a=a+1
        összes.append(Dobas)
    elif Dobas == 'I':
        b=b+1
        összes.append(Dobas)
    Vege=input('Nyomj ENTERT ha végeztél:')
print(a,'fejet dobtál!')
print(b,'írást dobtál!')
print(összes)
print('Ezeket dobtad sorrendbe')

    
