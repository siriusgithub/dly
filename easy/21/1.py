print('Program will take number, and give next highest number using same digits as given number.')
strnum = input('Enter number: ')

diglis = []

sta = strnum[-1]
pre = sta

nex = strnum[-2]

for pos in strnum:
    diglis.append(pre)
    diglis.sort(key=int)
    intpre = int(sta)
    intnex = int(nex)

    if intpre <= intnex:
       break
    elif intpre >= intnex:
         for itm in diglis:
             intitm = int(itm)
             if intnex < intitm:
