for num in range(99,0,-1):
    if num == 1:
       print("%d bottle of beer on the wall, %d bottle of beer. " \
             "Take it down, pass is around, now there are no bottles " \
             "of beer on the wall!"
             % (num,num)
             )

    elif num == 2:
         print("%d bottles of beer on the wall, %d bottles of beer. " \
               "Take one down, pass it around, %d bottle of beer on the wall!"
               % (num,num,(num - 1))
               ),

    else:
        print("%d bottles of beer on the wall %d bottles of beer. " \
              "Take one down, pass it around, %d bottles " \
              "of beer on the wall!" 
              % (num,num,(num - 1))
              ),
