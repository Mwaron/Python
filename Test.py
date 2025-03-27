nevek =  ["Éva", "Laci", "István", "Margit"]
magassag = [170, 190, 186, 164]
testtömeg = [70, 100, 80, 60]

"""Van-e olyan ember, akit Évának hívnak?"""
print("1. feladat")

if "Éva" in nevek:
    print("Van, olyan ember a nevek között akit Évának hívnak")
else:
    print("Nincs")


print("2. feladat")
m = 0
for i in magassag:
    if i > 165:
        m += 1

print(m, " ember magasabb, mint 165 cm")

print("3. feladat")
m = 0
for i in magassag:
    if i > m:
        m = i

print("A legmagasabb ember", m, "cm magas")

print("4. feladat")
s = 200
for i in testtömeg:
    if i < s:
        s = i

print("A soványabb ember", s, "kg")

print("5. feladat")
lm = 0
la = 2000
for i in magassag:
    if i > lm:
        lm = i
    elif i < la:
        la = i

print(lm-la, "cm")
