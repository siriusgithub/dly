#Input: number
#Output: the next prime number that uses the same set of digits

testNumber1 = "1101"   #1110
testNumber2 = "1011"   #1101
testNumber3 = "110011" #110101
testNumber4 = "001111" #010111
testNumber5 = "111100" #111100
testNumber6 = "01010"  #01100

testNumber7 = "1212211"
testNumber8 = ""
testNumber9 = "38576" #38675 #38765

#stringNumber = input('Enter number: ')

digitList = []
reversedDigitList = []

for position in testNumber2:
      digitList.append(int(position))

reversedDigitList = list(reversed(digitList))

previous = None
current = None
switch = False

for check in range(len(reversedDigitList)):
    previous = reversedDigitList[check]
    if switch == True:
        break
    for position in range(check, len(reversedDigitList)):
       if switch == True:
          break
       current = reversedDigitList[position]
       if current < previous:
          print("switch " + str(current) + " w/ " + str(previous))
          reversedDigitList[check] = current 
          #print(reversedDigitList[position])
          #print(reversedDigitList)
          reversedDigitList[position] = previous   
          #print(reversedDigitList[check])
          #print(reversedDigitList)
          switch = True
          
newDigitList = list(reversed(reversedDigitList))
for position in newDigitList:
    print(position, end='')

print('')

for position in reversedDigitList:
    if position < previous

# OUTPUTS
