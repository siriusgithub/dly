yea = input('Enter year: ')
mon = input('Enter month: ')
day = input('Enter day: ')

yea = int(yea)
mon = int(mon)
day = int(day)

if (yea % 400) == 0:
   lea = True
 
elif (yea % 100) == 0:
     lea = False
 
elif (yea % 4) == 0:
     lea = True
else:
    lea = False

jan = 1
feb = 2
mar = 3
apr = 4
may = 5
jun = 6
jul = 7
aug = 8
sep = 9
octobr = 10
nov = 11
dec = 12

if lea == True:
   dayjan = 31
   dayfeb = 29
   daymar = 31
   dayapr = 30
   daymay = 31
   dayjun = 30
   dayjul = 31
   dayaug = 31
   daysep = 30
   dayoctobr = 31
   daynov = 30
   daydec = 31

   if mon == jan:
      print(day)
   elif mon == feb:
        print(day + dayjan)
   elif mon == mar:
        print(day + dayjan + dayfeb)
   elif mon == apr:
        print(day + dayjan + dayfeb + daymar)
   elif mon == may:
        print(day + dayjan + dayfeb + daymar + dayapr)
   elif mon == jun:
        print(day + dayjan + dayfeb + daymar + dayapr + daymay)
   elif mon == jul:
        print(day + dayjan + dayfeb + daymar + dayapr + daymay + dayjun)
   elif mon == aug:
        print(day + dayjan + dayfeb + daymar + dayapr + daymay + dayjun + dayjul)
   elif mon == sep:
        print(day + dayjan + dayfeb + daymar + dayapr + daymay + dayjun + dayjul + dayaug)
   elif mon == octobr:
        print(day + dayjan + dayfeb + daymar + dayapr + daymay + dayjun + dayjul + dayaug + daysep)
   elif mon == nov:
        print(day + dayjan + dayfeb + daymar + dayapr + daymay + dayjun + dayjul + dayaug + daysep + dayoctobr)
   elif mon == dec:
        print(day + dayjan + dayfeb + daymar + dayapr + daymay + dayjun + dayjul + dayaug + daysep + dayoctobr + daynov)

elif lea == False:
     dayjan = 31
     dayfeb = 28
     daymar = 31
     dayapr = 30
     daymay = 31
     dayjun = 30
     dayjul = 31
     dayaug = 31
     daysep = 30
     dayoctobr = 31
     daynov = 30
     daydec = 31
     
     if mon == jan:
        print(day)
     elif mon == feb:
          print(day + dayjan)
     elif mon == mar:
          print(day + dayjan + dayfeb)
     elif mon == apr:
          print(day + dayjan + dayfeb + daymar)
     elif mon == may:
          print(day + dayjan + dayfeb + daymar + dayapr)
     elif mon == jun:
          print(day + dayjan + dayfeb + daymar + dayapr + daymay)
     elif mon == jul:
          print(day + dayjan + dayfeb + daymar + dayapr + daymay + dayjun)
     elif mon == aug:
          print(day + dayjan + dayfeb + daymar + dayapr + daymay + dayjun + dayjul)
     elif mon == sep:
          print(day + dayjan + dayfeb + daymar + dayapr + daymay + dayjun + dayjul + dayaug)
     elif mon == octobr:
          print(day + dayjan + dayfeb + daymar + dayapr + daymay + dayjun + dayjul + dayaug + daysep)
     elif mon == nov:
          print(day + dayjan + dayfeb + daymar + dayapr + daymay + dayjun + dayjul + dayaug + daysep + dayoctobr)
     elif mon == dec:
          print(day + dayjan + dayfeb + daymar + dayapr + daymay + dayjun + dayjul + dayaug + daysep + dayoctobr + daynov)
