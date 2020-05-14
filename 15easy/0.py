enter file name

open infil read only
inlis = infil.readlines()
open outfil write
outlis = []

input left or right justify

#left
if left justify (ie get rid of prefix spaces left of strings)
   for line in inlis
       for pos,char in enumerate(inlin)
           if char == space
              pass
           elif char != space
                #use pos to slice
                outstr = inlin[pos:-1]
                break
       outlis.append(outstr)

for lin in outlis:
    outfil.write(lin)

#right

if right justify(ie based on the longest string, move all other strings to that last index column
   
