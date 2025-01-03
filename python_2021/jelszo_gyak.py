jelszo = ('iamred12')
helyes = False
while False == helyes:
      a=input('Kérem a jelszót!\n')
      if a == jelszo:
            helyes = True
      else:
            print ('Helytelen jelszo')

   
helyes = False
while False == helyes:
      window=input('Hova szeretnél menni? Chrome, Games, Facebook\n')
      if window == 'Games':
            helyes = True
            print('launch of Valheim')
            print ('...')
            print('you wake up in your bed, and you go out')
            """go = input('write a w and press enter to walk 100 meters\n')
            if go == 'w':
                  print ('you meet with a bear')
                  hit=input('write "hit" to hit the bear\n')
                  if hit=='hit':
                        print ('you won you killed the bear')
                  else:
                        print('you didnt write the word hit')
            else:
                  print ('it s not a w')"""
      else:
            print ('Ez nem egy opcíó')
      
