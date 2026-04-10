tav = [12, 21, 49, 17, 25, 38, 19, 21, 51, 19]
idoZ = [12, 16, 65, 8, 36, 57, 20, 47, 95, 17]
idoB = [14, 28, 75, 5, 42, 47, 28, 32, 120, 17]

"""A. Mekkora távolságot kell megtenni, ha Kisnyékről szeretnénk eljutni Nagygyantéra"""
print("A. feladat:")
print(f"Kisnyéről Nagygyantéra {sum(tav)} km távolságot kell megtenni!")

"""B. Mekkora a legnagyobb távolság két egymást követő benzinkút között?"""
print("B feladat:")
print(f"Két egymást követő benzinkút között a legnagyobb a távolság: {min(tav)}")

"""C. Mekkora a legkisebb távolság két egymást követő benzinkút között?"""
print("C feladat:")
print(f"Két egymást követő benzinkút között a legkisebb a távolság: {min(tav)}")

"""D. Melyik két benzinkút között a legkisebb a távolság?"""
print("D feladat:")

i = tav.index(min(tav))
print(f"A(z) {i+1}. és a(z) {i+2}. benzinkút között a legkisebb a távolság.")

"""E. Hány benzinkút között nagyobb a távolság 30 km-nél?"""
print("E feladat:")

db = 0
for num in tav:
    if num > 30:
        db += 1
print(f"{db} benzinkút között nagyobb a távolság 30 km-nél.")

"""F. Az autóban, amivel elindultunk Kisnyékről 12 liter benzin van. Az autó fogyasztása 7 liter/100 
km. Meg kell-e állnunk valamelyik benzinkútnál tankolni, hogy eljussunk Nagygyantéra?"""

print("F feladat:")

if sum(tav) > (100/7)*12:
    print("Tankolnunk kell!")
else:
    print("Nem kell tankolnunk!")

"""G. Melyik két benzinkút között a legnagyobb a távolság?"""

print("G feladat:")

i = tav.index(max(tav))
print(f"A(z) {i+1}. és a(z) {i+2}. benzinkút között a legnagyobb a távolság.")


"""H. Mennyi idő alatt tette meg Zakariás a teljes utat?"""
print("H feladat:")

print(f"Zakariás {sum(idoZ)} perc alatt tette meg az utat!")

"""I. Mennyi idő alatt tette meg Bendegúz a teljes utat?"""
print("I feladat:")

print(f"Bendegúz {sum(idoB)} perc alatt tette meg az utat!")

"""J. Ki tette meg rövidebb idő alatt?"""
print("J feladat:")
Z = sum(idoZ)
B = sum(idoB)

if Z > B:
    print(f"Rövidebb idő alatt Bendegúz tette meg az utat")
else:
    print(f"Rövidebb idő alatt Zakariás tette meg az utat")

"""K. Bendegúznak hány perc volt az a legrövidebb idő, amit két benzinkút között tett 
meg?"""
print("K feladat:")
print(f" Bendegúz legrövidebb ideje: {min(idoB)} perc")

"""L. Zakariásnak hány perc volt az a leghosszabb ideje, amit két benzinkút között tett 
meg?"""
print("L feladat:")
print(f" Zakariás leghosszabb ideje: {max(idoZ)} perc")

""". Zakariásnak hány esetben fordult elő, hogy fél óránál hosszabb idő alatt sikerült 
teljesítenie a két benzinkút közötti távolságot?"""
print("M feladat:")
db = 0
for ido in idoZ:
    if ido > 30:
        db += 1
print(f"Zakariásnak {db} alkalommal volt fél óránál hosszabb az útja")

"""N. Válogasd szét két listába a 20 km alatti és a 20 km feletti távolságokat! Az értékeket 
írd ki a képernyőre egy sorba vesszővel elválasztva így:"""
print("N feladat:")

bigger = ""
smaller = ""

for num in tav:
    if num > 20:
        s = " " + str(num)
        bigger += s
    else:
        s = " " + str(num)
        smaller += s

print("20 km alattiak:",smaller, sep="")
print("20 km felettiek:",bigger, sep="")

"""O. Rendezd növekvő sorrendbe a Zakariáshoz tartozó időket! Az értékeket írd ki a 
képernyőre egy sorba vesszővel elválasztva így: """
print("O feladat:")

idoZ.sort()
print(" ".join(map(str, idoZ)))

"""P. Rendezd csökkenő sorrendbe a Bendegúzhoz tartozó időket! Az értékeket írd ki a 
képernyőre egy sorba vesszővel elválasztva így:"""
print("P feladat:")

csokkeno = sorted(idoB, reverse=True)
print(" ".join(map(str, csokkeno)))




