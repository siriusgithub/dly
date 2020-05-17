def nextPermutation(givenNumber):
    
    running = True
    digitList = list(str(givenNumber))
    
    for index in range(len(digitList)):
        digitList[index] = int(digitList[index])
    
    digitList.reverse()
    sortingList = []
    sortingList = []
    finalList = []
    
    for index in range(len(digitList)):
        for jndex in range(index, len(digitList)):
            #print("index: " + str(index))
            #print("jndex: " + str(jndex))
            if digitList[index] > digitList[jndex]:
               #print("before: ")
               #print(digitList)
               digitList.insert(jndex+1, digitList[index])
               #print(digitList)
               digitList.pop(index)
               #print("after: ")
               #print(digitList)
               for position in range(0, jndex):
                   sortingList.append(digitList[position])
               sorted(sortingList)
               sortingList.reverse()
               #print(sortingList)
               
               for position in range(len(sortingList)):
                   finalList.append(sortingList[position])
               for position in range(len(sortingList), len(digitList)):
                   finalList.append(digitList[position])
               running = False
               break
        if running == False: # Alternatively if not running:
           break
    
    digitList.reverse()
    
    digitList = ''.join(map(str, digitList))
    
    #print(int(digitList))
    
    finalList.reverse()
    
    finalList = ''.join(map(str, finalList))

    print(int(finalList))

#nextPermutation(38576) #38657
nextPermutation(37461) #37641 #37614