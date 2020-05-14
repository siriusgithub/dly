import random

# INCREMENTS
geninc = 0
leninc = 0
lis = ''

# NUMBER
print("\nGenerate how many passwords: ")
num = int(input())

# LENGTH
print("Length of password(s): ")
length = int(input())

# GENERATE
while geninc < num:
      leninc = 0
      tem = ''
      while leninc < length:
            tem += chr(random.randint(33, 125))
            leninc += 1
      lis += tem + '\n'
      geninc += 1

# PRINT
print('\n' + lis)

# SAVE
print("Save this list (y/n)?")
sav = input()

# YES
if sav == 'y':
   print("\nEnter path to save list to: ")
   pat = input()

   # ADD OR REWRITE
   print("\nRewrite this file (w) or append to it (a)?")
   typ = input()

   # WRITE
   if typ == 'w':
      outfil = open(pat,'w')
      outfil.write(lis)
      outfil.close()
      print('\n')
   
   # APPEND
   elif typ == 'a':
        outfil = open(pat,'a')
        outfil.write('\n' + lis)
        outfil.close()
        print('\n')

# NO
elif sav == 'n':
     print('\n')
     quit()
