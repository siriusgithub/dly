print('Takes a list and flips blocks of size x.')
print('EX:\n[1,2,3,4,5]\nx = 2')
print('[2,1,4,3,5]')

print('Press enter w/o entry when done.')

strlis = []

while True:
      itm = input('Enter item: ')
      if itm == '':
         break
      else:
          strlis.append(itm)

blk = input('Enter block size: ')
blk = int(blk)

inc = 1
temlis = []
finlis = []
lenstrlis = len(strlis)

for pos,itm in enumerate(strlis):
    temlis.append(itm)
    if inc == blk:
       temlis.reverse()
       for itm in temlis:
           finlis.append(itm)
       temlis = []
       inc = 1
    elif pos == (lenstrlis - 1):
         for itm in temlis:
             finlis.append(itm)
    else:
        inc += 1

print(finlis)
