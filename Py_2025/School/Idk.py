termek = ["toll", "ceruza", "radir", "tolltarto", "szovegkiemelo", "fuzet", "mappa", "kulcstarto", "bogre", "wekker"]
darabok=[23, 42, 59, 20, 10, 34, 10, 98, 123, 5]
arak=[282, 198, 410, 4320, 740, 900, 2300, 1861, 2000, 4900]

"""Hány darab terméket adtak el összesen? """
print("1. feladat")
print(max(darabok))


"""Mennyi a legdrágább termék ára? """
print("\n2. feladat")

osszeg=0
legdragabb = 0
for i, darab in enumerate(darabok):
    if darab * arak[i] > legdragabb:
        legdragabb = darab * arak[i]
    osszeg += darab * arak[i]


print(f'{legdragabb} Ft')

"""Mennyi bevétele volt ebben az órában a webáruháznak? """
print("\n3. feladat")

print(f'{osszeg} Ft')


"""Van-e az eladott termékek között szögmérő? A program vizsgálja meg
milyen termékek lettek eladva és az alapján adjon választ! """
print("\n4. feladat")

if "szögmérő" in termek:
    print("Van szögmérő")
else:
    print("Nincs szögmérő")

"""A programnak lehessen megadni billentyűzetről egy termék nevét és adjon választ,
hogy adtak-e el ebből a termékből a vizsgált időszakban, vagy sem!  """
print("\n5. feladat")

t = input("Termék neve: ")

if t in termek:
    print("Adtak el")
else:
    print("Nem adtak el")
