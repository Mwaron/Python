nev='Zoli'
kor=12
kerdes = str(nev) + ' most ' + str(kor) + ' éves!' + ' Hány éves lesz 2030-ban?\n'
kor2030 = input(kerdes)
kor2030=int(kor2030)
if kor2030==21:
    print('Helyes! Ügyes vagy!')
else:
    print('Ejnye! Ez nem sikerült!')
