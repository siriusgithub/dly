infil = open('numlis','r')

ins = ''

dat = infil.readlines()

#try:
#   for x in dat:
#       ins += (x[-4])
#       ins += '\n'
#except:
#      ins += 'NULL'

for x in dat:
    try:
       ins += (x[-4])
       ins += '\n'
    except:
          ins += 'NULL'
          ins += '\n'
          continue

infil.close()

outfil = open('lasnumlis','w')

outfil.write(ins)
outfil.close()
