# TODO MAKE SURE THAT RANGE CALCS ARE CORRECT
# DONE - TRY INT WORKS FOR NUMBERS, BUT OTHER SYMBOLS WILL PASS THE TEST AS WELL
# ABOVE WAS ACTUALLY DUE TO INCORRECT RANGE CALCULATION

print('Telephone Sanatizer')
telnum = input('Enter telephone number: ')

lentelnum = len(telnum)

if lentelnum > 14:
   print('Not a valid telephone number.')

elif lentelnum == 14:
     if telnum[0] == '(':
        for ind in range(1,4):
            tem = telnum[ind] 
            try:   
               tem = int(tem)
            except:
                  print('Not a valid telephone number.')
                  quit()
        if telnum[4] == ')':
           if telnum[5] == ' ':
              for ind in range(6,8):
                  tem = telnum[ind]
                  try:
                     tem = int(tem)
                  except:
                        print('Not a valid telephone number.')
                        quit()
              if telnum[9] == '-' or telnum[9] == '.':
                 for ind in range(10,14):
                     tem = telnum[ind]
                     try:
                        tem = int(tem)
                     except:
                           print('Not a valid telephone number.')
                           quit()
                 print('Valid telephone number.')
              else:
                  print('Not a valid telephone number.')
           else:
               print('Not a valid telephone number.')
        else:
            print('Not a valid telephone number.')
     else:
         print('Not a valid telephone number.')
        
elif lentelnum == 13:
     if telnum[0] == '(':
        for ind in range(1,4):
            tem = telnum[ind] 
            try:   
               tem = int(tem)
            except:
                  print('Not a valid telephone number.')
                  quit()
        if telnum[4] == ')':
           for ind in range(5,7):
               tem = telnum[ind]
               try:
                  tem = int(tem)
               except:
                     print('Not a valid telephone number.')
                     quit()
           if telnum[8] == '-' or telnum[8] == '.':
              for ind in range(9,13):
                  tem = telnum[ind]
                  try:
                     tem = int(tem)
                  except:
                        print('Not a valid telephone number.')
                        quit()
              print('Valid telephone number.')
           else:
               print('Not a valid telephone number.')
        else:
            print('Not a valid telephone number.')
     else:
         print('Not a valid telephone number.')

elif lentelnum == 12:
     for ind in range(0,3):
         tem = telnum[ind]
         try:
            tem = int(tem)
         except:
               print('Not a valid telephone number.')
               quit()
     if telnum[3] == '-' or telnum[3] == '.':
        for ind in range(4,7):
            tem = telnum[ind]
            try:
               tem = int(tem)
            except:
                  print('Not a valid telephone number.')
                  quit()
        if telnum[7] == '-' or telnum[7] == '.':
           for ind in range(8,12):
               tem = telnum[ind]
               try:
                  tem = int(tem)
               except:
                     print('Not a valid telephone number.')
                     quit()
           print('Valid telephone number')
        else:
            print('Not a valid telephone number.')
     else:
         print('Not a valid telephone number.')

elif lentelnum == 10:
     for ind in range(10):
         tem = telnum[ind]
         try:
            tem = int(tem)
         except:
               print('Not a valid telephone number.')
               quit()
     print('Valid telephone number.')

elif lentelnum == 8:
     for ind in range(2):
         tem = telnum[ind]
         try:
            tem = int(tem)
         except:
               print('Not a valid telephone number.')
               quit()
     if telnum[3] == '-' or telnum[3] == '.':
        for ind in range(4,8):
            tem = telnum[ind]
            try:
               tem = int(tem)
            except:
                  print('Not a valid telephone number.')
                  quit()
        print('Valid telephone number.')
     else:
         print('Not a valid telephone number.')

elif lentelnum == 7:
     for ind in range(7):
         tem = telnum[ind]
         try:
            tem = int(tem)
         except:
               print('Not a valid telephone number.')
               quit()
     print('Valid telephone number.')

else:
    print('Not a valid telephone number.')
