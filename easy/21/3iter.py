from itertools import permutations

# NUMBERS
# 38576
# 37461
# 28485

# UNORIGINAL PERMUTATION FUNCTION USING itertools MODULE
def n(numb):
    numb = str(numb)
    for i in sorted(permutations(numb)):
        permutation = int(''.join(i))
        if permutation > int(numb):
           print(permutation)
           break

# ORIGINAL PERMUTATION FUNCTION
def nextPermutation(givenNumber):
    print("O: " + str(givenNumber))
    # CONVERT givenNumber INTO STRING SO AS TO APPEND INDIVIDUAL CHARACTERS TO digitList
    digitList = list(str(givenNumber))
    
    # GO THROUGH digitList CONVERTING NUMBER STRING CHARACTERS TO INT
    for index in range(len(digitList)):
        digitList[index] = int(digitList[index])
    
    # START AT ONE'S PLACE IN givenNumber
    digitList.reverse()

    # DECLARING LISTS
    sortingList = []
    sortingList = []
    finalList = []
    
    # COMPARISON LOOPS
    # BREAK VARIABLE
    running = True
    # FIRST LOOP
    for aindex in range(len(digitList)):
        # SECOND LOOP OFFSET BY ONE INDEX AKA STARTING AT INDEX ONE
        for bindex in range(aindex, len(digitList)):
            print("aindex: " + str(aindex) , "value: " + str(digitList[aindex]))
            print("bindex: " + str(bindex) , "value: " + str(digitList[bindex]))
            # IF ONES PLACE IS GREATER THAN TENS PLACE
            if digitList[aindex] > digitList[bindex]:
               print("before: ", end='')
               print(digitList)
               digitList.insert(bindex+1, digitList[aindex])
               print("after: ", end='')
               print(digitList)
               digitList.pop(aindex)
               print(digitList)
               for position in range(0, bindex):
                   sortingList.append(digitList[position])

               sorted(sortingList)
               sortingList.reverse()
               print(sortingList)
               
               for position in range(len(sortingList)):
                   finalList.append(sortingList[position])

               for position in range(len(sortingList), len(digitList)):
                   finalList.append(digitList[position])

               # SET BREAK VARIABLE TO END LOOPING
               running = False
               break

        # END LOOPING
        if running == False: # Alternatively if not running:
           break
    
    digitList.reverse()
    
    digitList = ''.join(map(str, digitList))
    
    #print(int(digitList))
    
    finalList.reverse()
    
    finalList = ''.join(map(str, finalList))

    print("N: " + str(int(finalList)))

# SINGLE TESTING
nextPermutation(69657)

# LIST TESTING
testNumberList = [69657, 38563, 71025, 82436, 60762, 49886, 28485, 88757, 43451, 84704]

# COMPARE CORRECT FUNCTION, n(), TO OUR TEST ONE, nextPermutation()
#for testNumber in testNumberList:
#     print('C: ', end='')
#     n(testNumber)
#     print('O: ', end='')
#     nextPermutation(testNumber)
#     print('')
