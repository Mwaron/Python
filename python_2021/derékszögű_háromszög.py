a=input('a=')
b=input('b=')
c=input('c=')
a=int(a)
b=int(b)
c=int(c)
if a+b>c:
    if a+c>b:
        if b+c>a:
            print('Lehet ebből háromszöget szerkeszteni')

            if a*a+b*b==c*c:
                print('Ez egy derékszögű háromszög')
            elif a*a+c*c==b*b:
                print('Ez egy derékszögű háromszög')
            elif b*b+c*c==a*a:
                print('Ez egy derékszögű háromszög')
            else:
                print('Ez nem egy derékszögű háromszög')
        else:
            print('Nem lehet ebből háromszöget szerkeszteni')
    
    else:
        print('Nem lehet ebből háromszöget szerkeszteni')
    
else:
    print('Nem lehet ebből háromszöget szerkeszteni')
