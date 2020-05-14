print('Takes a file and left/right justifies the text')
strpth = input('Enter file path: ')
infil = open(strpth,'r')
inlis = infil.readlines()

print('File will be saved as %sjustified' % strpth)

outfil = open((strpth + 'justified'),'w')
outlis = []

print('Left justify (l) or right justify (r)?')
jusdir = input('Enter: ')

if jusdir == 'l':
   for inlin in inlis:
       for pos,char in enumerate(inlin):
           if char == ' ':
              pass
           elif char != ' ':
                outlin = inlin[pos:-1]
                break
       outlis.append(outlin)

   for lin in outlis:
       outfil.write(lin + '\n')

if jusdir == 'r':
   col = 0
   for inlin in inlis:
       if len(inlin) > col:
          col = len(inlin)

   for inlin in inlis:
       if len(inlin) <= col:
          numspc = col - len(inlin)
          outlin = ' ' * numspc + inlin[0:]
       outlis.append(outlin)

   for lin in outlis:
       outfil.write(lin)

infil.close()
outfil.close()

print('Done')
