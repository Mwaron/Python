print('Az első 10db 3-mal osztható szám')
szamok = []
a = 3
while 10 >= len(szamok):
    if a % 3 == 0:
        szamok.append(a)
    a=a+1
print(szamok)
