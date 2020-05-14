for num in range(100,0,-1):
    if num == 1:
       print("1 bottle of beer on the wall, one bottle of beer. Take it down, pass it around, now " \
             "there are no more bottles of beer on the wll!")
    elif num == 2:
         print("2 bottles of beer on the wall, two bottles of beer. Take one down, pass it around, " \
               "now there's just one bottle of beer on the wall!")
    else:
        print("%d bottles of beer on the wall, %d bottles of beer. Take one down, pass it around, " \
              "%d bottles of beer on the wall!" % (num , num , (num - 1)))
