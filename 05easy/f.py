import getpass
import hashlib

# MAIN
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

# PASS
if usrexi == True:

   # QUERY PASS
   pas = getpass.getpass('Password: ')

   # HASH ENTERED PASS
   pas = pas.encode('utf-8')
   haspas = hashlib.sha512(pas).hexdigest()

   # PASS POSITION IN INFIL LIST
   reapaspos = lis.index(usr)
   reapaspos = reapaspos + 1

   # GET PASS
   reapasnew = lis[reapaspos]

   # CONVERT REAL PASS TO LIST
   lisreapasnew = list(reapasnew)

   # GET LENGTH OF PASS PLUS NEWLINE
   lenlisreapasnew = len(lisreapasnew)

   # DETERMINE CUTOFF
   lenreapas = lenlisreapasnew - 2

   inc = 0
   reapas = ''
   while inc <= lenreapas:
         reapas += lisreapasnew[inc]
         inc += 1

   if haspas == reapas:
      print('Logged In')
   else:
       print('Incorrect Password')
       quit()

else:
    print('Username does not exist.')
    infil.close()
    quit()

logout = False
while logout == False:
      print('Log out (l), create new user (c), or delete a user (d)?')
      opt = input()

      if opt == 'l':
         quit()

      elif opt == 'c':
           print('Enter username for new user:')
           newusr = input()
           newusr = newusr + '\n'

           if newusr in lis:
              print('User already exists.')
              quit()

           print('Enter password for new user:')
           newpas = input()
           newpas = newpas.encode('utf-8')
           newhaspas = hashlib.sha512(newpas).hexdigest()

           infil.close()
           outfil = open('list','a')
           outfil.write(newusr)
           outfil.write(newhaspas)
           outfil.write('\n')
           outfil.write('\n')
           outfil.close()

      elif opt == 'd':
           print('Enter username for user to be deleted:')
           delusr = input()
           delusr = delusr + '\n'
           infil.close()
           infil = open('list','r')
           fil = infil.readlines()
           infil.close()
           outfil = open('list','w')

           delusrpos = fil.index(delusr)
           delpaspos = delusrpos
           delnewpos = delusrpos
           del fil[delusrpos]
           del fil[delpaspos]
           del fil[delnewpos]

           for lin in fil:
               outfil.write(lin)

           outfil.close() 
