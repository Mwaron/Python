print("Dobj kockával és lássuk jól működik-e")
dobasok = [0,0,0,0,0,0] #itt számoljuk melyik számot hányszor dobtuk meg 
ertek = input("Hanyast dobtál? ")
while ertek != "":
    if ertek == "1":
        dobasok[0] = dobasok[0] + 1 # a lista első eleme a 0 indexen van
    elif ertek == "2":
        dobasok[1] = dobasok[1] + 1
    elif ertek == "3":
        dobasok[2] = dobasok[2] + 1
    elif ertek == "4":
        dobasok[3] = dobasok[3] + 1
    elif ertek == "5":
        dobasok[4] = dobasok[4] + 1
    elif ertek == "6":
        dobasok[5] = dobasok[5] + 1
    else :
        print("Valamit elrontottál ilyen dobás nem létezik")

    ertek = input("Rendben. Most hanyast dobtál? (ha nincs több csak üss ENTERt)")
   
dobasok_szama = dobasok[0]+dobasok[1]+dobasok[2]+dobasok[3]+dobasok[4]+dobasok[5]
print("Összesen", dobasok_szama, "-szor dobtál.")
print("Egyest:",  dobasok[0])
print("Kettest:", dobasok[1])
print("Hármast:", dobasok[2])
print("Négyest:", dobasok[3])
print("Ötöst:",   dobasok[4])
print("Hatost:",  dobasok[5])
