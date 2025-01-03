a=int (input('Kérek egy számot: '))
b=2
c=0
while(b < a):
    if (a%b == 0):
        print ('ez nem egy prím szám, egyen és önmagán kivüli pozitív osztója:',b )
        c=c+1
    b=b+1
if (c == 0): 
    print ('Ez egy prím szám')
