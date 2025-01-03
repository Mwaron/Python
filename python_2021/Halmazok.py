passziv = {'bárány','csirke','falusi','tehén'}
print(passziv)
print('Adj hozzá még három passzív mobot a minecraftból')
a=1
while a <= 3:
        c=str(a)
        b = input(c+':')
        passziv.add(b)
        a=a+1
print('A passzív mobok',passziv)
semleges = {'enderman','méh','piglin'}
ellenseges = {'boszorkany','creeper','csontvaz','zombi'}
lenyek = semleges.union(ellenseges,passziv)
print('Az összes mob:')
print(lenyek)
allatok = {"kecske", "méh","tehén", "birka", "kutya", "ló"}
metszet = allatok.intersection(lenyek)
print('Amik a való világban is vannak és most felsoroltad itt is:')
print(metszet)
