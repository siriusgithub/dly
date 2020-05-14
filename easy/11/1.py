print('Find what day a certain date was.')

yea = input('Enter year: ')
mon = input('Enter month: ')
day = input('Enter day: ')

try:
   yea = int(yea)
except:
      print('Non-valid year.')

try:
   mon = int(mon)
except:
      print('Non-valid month.')

try:
   day = int(day)
except:
      print('Non-valid day.')

if (yea % 400) == 0:
   lea = True
   break

elif (yea % 100) == 0:
     lea = False
     break

elif (yea % 4) == 0:
     lea = True
     break
   
else:
    lea = False
