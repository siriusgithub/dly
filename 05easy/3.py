# must login first to delete/create usr
import getpass
import hashlib

# MAIN
print('Login (l), create new user (c), or delete a user (d)?')
opt = input()

# LOGIN
if opt == 'l':

   # OPEN USR/PASS FILE
   infil = open('list','r+')
   lis = infil.readlines()

   # ASK USR
   usr = input('Username: ')
   usr = usr + '\n'

   # QUERY USR
   if usr in lis:
      usrexi = True
   else:
       usrexi = False

   if usrexi == True:
      pas = getpass.getpass('Password: ')
      num = lis.index(usr)
      num = num + 1
      reapas = lis[num]
      lisreapas = list(reapas)
      lenlisreapas = len(lisreapas)
      cutoff = lenlisreapas - 3
      pos = 0
      tem = ''
      while pos <= cutoff:
            tem += lisreapas[pos]
            pos += 1
      if pas == tem:
         print('finally done')
      else:
          print('needs more work')
          
# find out number of items in list, and then get rid of the two ends \ and n
      
      
#      pas = pas.encode('utf-8')
   else:
       print('Username does not exist.')
       quit()

#   haspas = hashlib.sha512(pas).hexdigest()

   print(lis.index(usr))
   print(lis)
