print('Enter username for user to be deleted:')
delusr = input()
delusr = delusr + '\n'
outfil = open('list','r')
fil = outfil.readlines()
outfil.close()
outfil = open('list','w')
print(fil)
delusrpos = fil.index(delusr)
print(delusrpos)
delpaspos = delusrpos + 1
print(delpaspos)
delnewpos = delpaspos + 1
print(delnewpos)
del fil[delusrpos]
#del fil[delpaspos]
#del fil[delnewpos]
print(fil)

for lin in fil:
    outfil.write(lin)

outfil.close() 
