nam = input('Name: ')
age = input('Age: ')
use = input('User: ')

print('Your name is %s, you are %s years old, and your reddit username is %s.' % (nam,age,use))

outfil = open('list0','a')

ins = 'Name: %s\nAge: %s\nUser: %s\n\n' % (nam,age,use)

outfil.write(ins)
outfil.close()
