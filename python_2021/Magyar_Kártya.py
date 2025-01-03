kartya = 'ZF'
print('Gondoltam egy magyar kártyára, ki tudod találni?')
print('Választékok:')
print('Piros Ász')
print('Zöld Ász')
print('Tök Ász')
print('Makk Király')
print('Piros Felső')
print('Makk Felső')
print('Zöld Felső')
print('Tök Felső')
print('Tök Alsó')
print('Elég a rövidítésüket írni pl: PÁ,(Piros Ász)')
szöveg = input('Mire gondoltam?\n')
while szöveg != kartya:
    szöveg = input('Sajnos nem jó! Próbáld újra: ')
print('Eltaláltad! :D')
input('Nyomj entert a bezáráshoz')
    
