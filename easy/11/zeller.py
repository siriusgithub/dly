# PYTHON IMPLEMENTATION OF ZELLER'S RULE BY SIRIUS

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

yea = str(yea)

# 01 = Janurary  = 11
# 02 = Feburary  = 12
# 03 = March     = 01
# 04 = April     = 02
# 05 = May       = 03
# 06 = June      = 04
# 07 = July      = 05
# 08 = August    = 06
# 09 = September = 07
# 10 = October   = 08
# 11 = November  = 09
# 12 = December  = 10

if day > 31:
   print('Not a valid date.')
   quit()

k = day

if mon == 1:
   mon = 11
elif mon == 2:
     mon = 12
elif mon == 3:
     mon = 1
elif mon == 4:
     mon = 2
elif mon == 5:
     mon = 3
elif mon == 6:
     mon = 4
elif mon == 7:
     mon = 5
elif mon == 8:
     mon = 6
elif mon == 9:
     mon = 7
elif mon == 10:
     mon = 8
elif mon == 11:
     mon = 9
elif mon == 12:
     mon = 10
else:
    print('Not a valid date.')
    quit()

m = mon

if len(yea) > 4:
   print('Program can only go to the 99th century.')
   quit()

D = yea[2] + yea[3]
D = int(D)

if m == 11 or m == 12:
   D = D - 1

C = yea[0] + yea[1]
C = int(C)

f = k + (int((13*m-1)/5)) + D + (int(D/4)) + (int(C/4)) - 2*C

rem = f % 7

if rem == 0:
   print('Sunday')
elif rem == 1:
     print('Monday')
elif rem == 2:
     print('Tuesday')
elif rem == 3:
     print('Wednesday')
elif rem == 4:
     print('Thursday')
elif rem == 5:
     print('Friday')
elif rem == 6:
     print('Saturday')
