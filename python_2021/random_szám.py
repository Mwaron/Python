print("Szia! Neked kik a kedvenc marvel szereplőid?")
hosok = [] # üres lista létrehozása
nev = input("Hős neve:")
while nev != "":
    hosok.append(nev)
    nev = input("Van még kedvenced? (ha nincs több csak üss ENTERt)  
                 \nHős neve:")

print("Összesen:", len(hosok), "nevet adtál meg.")
print("Ezek sorban a következők:")
print(hosok)
