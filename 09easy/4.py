# TODO INTEGRATE FILE FEATURE FOR LONG STRINGS W/ NEWLINES IN THEM
# TODO MAKE SURE THAT .SORT IS USING ASCII VALUES, IF TIME ALLOWS THEN JUST PARSE THE STRINGS AND SORT YOURSELF

print('\nCharacter defined as any ASCII character.\nString defined as any grouping of ASCII characters without any spaces.\nStrings defined as any grouping of ASCII characters with a space at either the beginning or end, or at both ends.\nDigits defined as ASCII characters 0,1,2,3,4,5,6,7,8, and 9.\nNumber defined as any grouping of ASCII characters without any spaces.\nNumbers defined as any grouping of ASCII characters 0-9 with a space at either the beginning or end, or at both ends.'
      )
       
print('\nArrange characters (c), strings (s), digits (d), or numbers (n)?')
opt = input()

# CHARACTERS
if opt == 'c':
   print('\nASCII values will be assigned to each character.\nArrange from low values to high values (l) or high values to low values (h)?'
         )
   sor = input()

   if sor == 'l':
      strinp = input('\nEnter characters: ')
      ordlis = []
      chrlis = []

      for pos in strinp:
          ordlis.append(ord(pos))
          
      ordlis.sort()

      for pos in ordlis:
          if pos == 32:
             chrlis.append('space')
          else:
              chrlis.append(chr(pos))

      inc = 1
      addinc = 0
      sto = len(chrlis)

      for pos,char in enumerate(chrlis):
          if pos == sto - 1:
             addinc += inc
             print('x' + str(inc) , char)
          elif chrlis[pos] != chrlis[pos+1]:
               print('x' + str(inc) , char)
               addinc += inc
               inc = 1
          else:
              inc += 1

      print('\n' + str(addinc) , 'total characters.\n')
             

   if sor == 'h':
      strinp = input('\nEnter characters: ')
      ordlis = []
      chrlis = []

      for pos in strinp:
          ordlis.append(ord(pos))

      ordlis.reverse()

      for pos in ordlis:
          if pos == 32:
             chrlis.append('space')
          else:
              chrlis.append(chr(pos))

      inc = 1
      addinc = 0
      sto = len(chrlis)

      for pos,char in enumerate(chrlis):
          if pos == sto - 1:
             addinc += inc
             print('x' + str(inc) , char)
          elif chrlis[pos] != chrlis[pos+1]:
               print('x' + str(inc) , char)
               addinc += inc
               inc = 1
          else:
              inc += 1

      print('\n' + str(addinc) , 'total characters.\n')

# STRINGS
elif opt == 's':
     print('\nASCII values will be assigned to each character.\nArrange from low values to high values (l) or high values to low values (h)?')

     sor = input()

     if sor == 'l':
        strinp = input('\nEnter strings: ')
        lis = strinp.split()

        lis.sort()

        ordlis = lis     

        inc = 1
        addinc = 0
        sto = len(ordlis)

        for pos,strg in enumerate(ordlis):
            if pos == sto - 1:
               addinc += inc
               print('x' + str(inc) , strg)
            elif ordlis[pos] != ordlis[pos+1]:
                 print('x' + str(inc) , strg)
                 addinc += inc
                 inc = 1
            else:
                inc += 1

        print('\n' + str(addinc) , 'total strings.\n')

     if sor == 'h':
        strinp = input('\nEnter strings: ')
        lis = strinp.split()

        lis.reverse()

        ordlis = lis     

        inc = 1
        addinc = 0
        sto = len(ordlis)

        for pos,strg in enumerate(ordlis):
            if pos == sto - 1:
               addinc += inc
               print('x' + str(inc) , strg)
            elif ordlis[pos] != ordlis[pos+1]:
                 print('x' + str(inc) , strg)
                 addinc += inc
                 inc = 1
            else:
                inc += 1

     print('\n' + str(addinc) , 'total strings.\n')



# DIGITS
elif opt == 'd':
     pass

# NUMBERS
elif opt == 'n':
     pass

