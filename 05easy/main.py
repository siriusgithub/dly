import getpass
import hashlib

# MAIN
print('Login (l), create new user (c), or delete a user (d)?')
act = input()

# LOGIN
if act == 'l':

   infil = open('list','r+')
   lis = infil.read()
   lin = infil.readlines()

   use = input('Username: ')
   use = use + '\n'

   if use in lis:
      useexi = True
   else:
       useexi = False

   if useexi == True:
      pas = getpass.getpass('Password: ')
      pas = pas.encode('utf-8')
   else:
       print('Username does not exist.')
       quit()

   haspas = hashlib.sha512(pas).hexdigest()

for new in :
    if use in lincon:
       print(num)
