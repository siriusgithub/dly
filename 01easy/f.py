nam = input('Name: ')
age = input('Age: ')
use = input('User: ')

while True:
     print('\nWrite to list?')
     con = input('y/n: ')
     if con == 'y' or con == 'Y':
        break
     elif con == 'n' or con == 'N':
          quit()
     else:
         continue

outfil = open('list','a')

ins = 'Name: %s\nAge: %s\nUser: %s\n\n' % (nam,age,use)

outfil.write(ins)
outfil.close()
