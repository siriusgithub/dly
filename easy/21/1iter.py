def nextPermutation(number):
    
    running = True
    number = list(str(number))
    
    for index in range(len(number)):
        number[index] = int(number[index])
    
    number.reverse()
    
    for index in range(len(number)):
        for jndex in range(len(number)-index):
            if number[index] > number[jndex]:
                number.insert(jndex+1, number[index])
                number.pop(index)
                running = False
                break
        if running == False: # Alternatively if not running:
            break
    
    number.reverse()
    
    number = ''.join(map(str, number))
    
    print(int(number))

nextPermutation(38576)
