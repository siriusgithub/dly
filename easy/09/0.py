print("Arrange digits (d), arrange numbers (n), arrange letters (l), or arrange words (w)?")
opt = input()

if opt == 'd':
   print('\nArrange from low to high (l) or from high to low (h)?')
   arr = input()

   if arr == 'l':
      lis = input('\nEnter digits: ')
      lis = list(lis)

      print('\n')

      lis.sort()

      print(lis)

      for pos,num in enumerate(lis):
          # interesting usage of and here instead of or
          if num != '0' and num != '1':
             continue
          print(num,end = ' ')
      
      print('\n')

   if arr == 'h':
      lis = input('Enter digits: ')
      lis = list(lis)

      print('\n')

      lis.reverse()

      for pos,num in enumerate(lis):
          if num == ' ':
             continue
          else:
              print(num,end = ' ')

      print('\n')

if opt == 'n':
   print("Arrange from low to high (l)|from high to low (h)?")
   arr = input()

   if arr == 'l':
      lis = input('Enter numbers separated by spaces: ')
