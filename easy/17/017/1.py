hei = input('Enter height of triangle: ')
hei = int(hei)

while True:
      drwchr = input('Enter single character to draw with: ')
      if len(drwchr) == 1:
         break
      else:
          print('More than one character.')

print('\nHave the point on top (t) or bottom (b)?')
print('                       @             @@@@\n' \
      '                       @@            @@  \n' \
      '                       @@@@          @   ')

pos = input('Enter: ')

print('\nLeft justify (l) or right justify (r)?')
print('              @                    @\n' \
      '              @@                  @@\n' \
      '              @@@@              @@@@')
jus = input('Enter: ')

if pos == 't':
   if jus == 'l':
      inc = 1
      for lin in range(hei):
          print(drwchr * inc)
          inc = inc * 2
          
   elif jus == 'r':
        inc = 1
        for lin in range(hei):
            inc = inc * 2
        lonlin = int(inc / 2)

        inc = 1
        for lin in range(hei):
            print(' ' * (lonlin - inc) + (drwchr * inc))
            inc = inc * 2

if pos == 'b':
   if jus == 'l':
      inc = 1
      for lin in range(hei):
          inc = inc * 2
      inc = int(inc / 2)

      for lin in range(hei):
          print(drwchr * inc)
          inc = int(inc / 2)

   if jus == 'r':
      inc = 1
      for lin in range(hei):
          inc = inc * 2
      inc = int(inc / 2)
      lonlin = inc

      for lin in range(hei):
          print(' ' * (lonlin - inc) + (drwchr * inc))
          inc = int(inc / 2)
      

print('\nDone')
