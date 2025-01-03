szam = 4
print("Szia! \nJátszunk egy játékot! \nGondolok egy számra és te megpróbálod kitalálni.")
print("\nKezdhetjük, gondoltam egy számra 1 és 5 között...")

tipp = input("Tippelj: ")
tipp = int(tipp)

while tipp != szam :
    print("Sajnos nem talált, de próbáld újra!")
    tipp = int(input("Tippelj: "))

print("Eltaláltad! Ügyes vagy!")
