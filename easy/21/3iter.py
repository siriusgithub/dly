from itertools import permutations

# DEBUG NUMBERS
# 38576
# 37461
# 28485
# 342
# 5342

# UNORIGINAL PERMUTATION FUNCTION USING itertools MODULE
def correctPermutation(givenNumber):
    # CONVERT INT TO STRING SINCE INT IS NOT ITERABLE
    strNumber = str(givenNumber)

    # CREATE ALL PERMUTATIONS USING ITERABLE DIGITS FROM numb AND SORT
    for index in sorted(permutations(strNumber)):
        # CONVERT INDEX INTO SINGLE FULL STRING THEN INTO INT
        permutation = int(''.join(index))
        # FROM THE SORTED PERMUTATION LIST FIND THE NEXT HIGHEST AFTER givenNumber
        if permutation > givenNumber:
           print(permutation)
           break

# ORIGINAL PERMUTATION FUNCTION
def nextPermutation(givenNumber):
    # CONVERT givenNumber INTO STRING SO AS TO APPEND INDIVIDUAL CHARACTERS TO digitList
    digitList = list(str(givenNumber))
    
    # GO THROUGH digitList CONVERTING EACH CHARACTER STRING TO INT
    for index in range(len(digitList)):
        digitList[index] = int(digitList[index])
    
    # START AT ONES PLACE IN givenNumber
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
            # WE NEED TO COMPARE SEPERATED PLACES, CURRENT THE IF STATEMENT ONLY DOES THE FOLLOWING:
            # IF ONES PLACE IS GREATER THAN TENS PLACE
            # IF TENS PLACE IS GREATER THAN HUNDREDS PLACE
            # IF HUNDREDS PLACE IS GREATER THAN THOUSANDS PLACE
            # ETC., WHICH ARE ALL RIGHT NEXT TO EACH OTHER
            if digitList[aindex] > digitList[bindex]:
               print("before: ", end='')
               print(digitList)
               digitList.insert(bindex+1, digitList[aindex])
               print("after: ", end='')
               print(digitList)
               digitList.pop(aindex)
               print("after: ", end='')
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
    
    # REORIENT LIST THE CORRECT WAY
    finalList.reverse()
    
    # TURN finalList INTO STRING
    finalOutput = ''.join(map(str, finalList))

    # PRINT ORIGINAL NUMBER
    print("O: " + str(givenNumber))

    # PRINT SOLUTION
    print("N: " + str(int(finalOutput)))

# SINGLE TESTING
nextPermutation(69657)
#correctPermutation(69657)

# LIST TESTING
#testNumberList = [69657, 38563, 71025, 82436, 60762, 49886, 28485, 88757, 43451, 84704]
#
# COMPARE CORRECT FUNCTION, correctPermutation(), TO OUR TEST ONE, nextPermutation()
#for testNumber in testNumberList:
#     print('C: ', end='')
#     correctPermutation(testNumber)
#     print('O: ', end='')
#     nextPermutation(testNumber)
#     print('')
