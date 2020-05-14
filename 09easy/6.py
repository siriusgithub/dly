# TODO

print('\nCharacter defined as any ASCII character.' , end='')
print('\n\nString defined as any grouping of ASCII characters without any spaces.' , end='')
print('\nStrings defined as any grouping of ASCII characters with a space at either ' , end='')
print('the beginning or end, or at both ends' , end='')

print('\n\nDigits defined as ASCII characters 0,1,2,3,4,5,6,7,8, and 9.' , end='')
print('\n\nNumber defined as any grouping of ASCII characters 0-9 without any spaces and ' , end='')
print('either having a single period or not.')

print('\nNumbers defined as any grouping of ASCII characters 0-9 with a space at either ' , end='')
print('the beginning or end, or at both ends; and either having a single period or not.')

print('\nArrange characters (c), strings (s), digits (d), or numbers (n)?')

opt = input()

if opt == 'c' or opt == 's':
   print('\nASCII values will be assigned to each character.')
   print('Arrange from low values to high values (l) or high values to low values (h)?')

   sor = input()

   if sor == 'l' or sor == 'h':
      if opt == 'c':
         strinp = input('\nEnter characters: ')
      elif opt == 's':
         strinp = input('\nEnter strings: ')

      ordlis = []
      chrlis = []

      for pos in strinp:
          ordlis.append(ord(pos))

      ordlis.sort()

      if sor == 'h':
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
          elif chrlis[pos] != chrlis[pos + 1]:
               print('x' + str(inc) , char)
               addinc += inc
               inc = 1
          else:
              inc += 1

      print('\n' + str(addinc) , 'total character(s).\n')
