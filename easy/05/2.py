import getpass
import hashlib

# MAIN
print('Login (l), create new user (c), or delete a user (d)?')
act = input()

# LOGIN
if act == 'l':

   infil = open('list','r+')
   lin = infil.readlines()

   use = input('Username: ')
   use = use + '\n'

   if use in lin:
      useexi = True
   else:
       useexi = False

   if useexi == True:
      pas = getpass.getpass('Password: ')
#      pas = pas.encode('utf-8')
   else:
       print('Username does not exist.')
       quit()

#   haspas = hashlib.sha512(pas).hexdigest()

   print(lin.index(use))
   print(lin)

# get index then add one for password
