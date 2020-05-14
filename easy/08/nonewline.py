for x in range(99,0,-1):
    #if not x - 1:
    if x == 1:
        print "%d bottle of beer on the wall, %d bottle of beer.  Take one " \
              "down pass it around, now theres no more bottles of " \
              "beer on the wall :(" % (x, x)
    elif x == 2:
        print "%d bottles of beer on the wall, %d bottles of beer.  Take one " \
              "down pass it around, %d bottle of beer on the wall! " \
              % (x, x,x-1),
    else:
        print "%d bottles of beer on the wall, %d bottles of beer.  Take one " \
              "down pass it around, %d bottles of beer on the wall! " \
              % (x, x,x-1),
