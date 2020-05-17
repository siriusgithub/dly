def nextPermutation(givenNumber):
    
    running = True
    digitList = list(str(givenNumber))
    
    for index in range(len(digitList)):
        digitList[index] = int(digitList[index])
    
    digitList.reverse()
    
    for index in range(len(digitList)):
        for jndex in range(len(digitList) - index):
            print("index: " + str(index))
            print("jndex: " + str(jndex))
            if digitList[index] > digitList[jndex]:
               print("before: ")
               print(digitList)
               digitList.insert(jndex+1, digitList[index])
               print(digitList)
               digitList.pop(index)
               print("after: ")
               print(digitList)
               running = False
               break
        if running == False: # Alternatively if not running:
           break
    
    digitList.reverse()
    
    digitList = ''.join(map(str, digitList))
    
    print(int(digitList))

nextPermutation(37461) #37641 #37614