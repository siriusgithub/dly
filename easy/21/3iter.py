from itertools import permutations

# NUMBERS
# 38576
# 37461

def n(numb):
    numb = str(numb)
    for i in sorted(permutations(numb)):
        permutation = int(''.join(i))
        if permutation > int(numb):
           print(permutation)
           break

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

NEW FAV ANNOYING NUMBER  ->  28485

#testNumberList = [69657, 38563, 71025, 82436, 60762, 49886, 28485, 88757, 43451, 84704]

#for testNumber in testNumberList:
#    print('Correct: ')
#    n(testNumber)
#    nextPermutation(testNumber)
#    print('Ours: ')
#    print('')
