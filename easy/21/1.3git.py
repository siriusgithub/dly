# Input: number
# Output: the next prime number that uses the same set of digits

# BINARY
testNumber1 = '1101'   #1110
testNumber2 = '1011'   #1101
testNumber3 = '110011' #110101
testNumber4 = '001111' #010111
testNumber5 = '111100' #111100
testNumber6 = '01010'  #01100

# 123
testNumber7 = '1212211' #1221112
testNumber8 = '123321' #131223 # find the next smallest postion that is larger than the main swap
                               # to swap with, then go from smallest to largest with largest in the ones place

# DECIMAL
testNumber9 = '38576' #38657 not 38675 we forgot about 57
testNumber10 = '385766' #386567

# DLY FUNCTION
def next(givenNumber):
    str(givenNumber)

    # LISTS ASSIGNMENT & SETUP
    digitList = []
    sortedDigitList = []
    nextHighestList = []
    
    for character in givenNumber:
        digitList.append(int(character))
    
    reversedDigitList = list(reversed(digitList))
    
    # VARIABLE ASSIGNMENT
    done = False
    previousReversed = None

    # PARSING THROUGH GIVEN NUMBER
    while done == False:
          for currentReversed in reversedDigitList:
              if previousReversed == None:
                 previousReversed = currentReversed
              elif previousReversed <= currentReversed:
                   print(previousReversed)
                   sortedDigitList.append(previousReversed)
                   sorted(sortedDigitList)
              elif previousReversed > currentReversed:
                   for currentSorted in sortedDigitList:
                       if currentSorted <= currentReversed:
                          continue
                       elif currentSorted > currentReversed:
                            print(currentReversed)
                            done = True
              previousReversed = currentReversed


# PERM FUNCTION
def n():
    from itertools import permutations
    numb = input('Enter your number: ')
    for i in sorted(permutations(numb)):
        permutation = int(''.join(i))
        if permutation > int(numb):
           print(permutation)
           break

#n()
next(testNumber9)
