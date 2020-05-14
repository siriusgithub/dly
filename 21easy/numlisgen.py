from random import randint

outfil = open('numlis','w')

ins = ''

for x in range(0,100):
    ins += str(randint(0,9999))
    ins += '\n'

outfil.write(ins)
outfil.close()

