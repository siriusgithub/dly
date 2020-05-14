#######################################################################################################
#You're challenge for today is to create a random password generator!                                 #
#For extra credit, allow the user to specify the amount of passwords to generate.                     #
#For even more extra credit, allow the user to specify the length of the strings he wants to generate!#
#######################################################################################################
import random

print('Enter number of passwords to generate: ')
numPasswords = int(input())
print('Enter length of passwords: ')
lengthPasswords = int(input())

numPasswordsInc = 0
lengthPasswordsInc = 0
listPasswords = ''

while numPasswordsInc < numPasswords:
	lengthPasswordsInc = 0
	tempPassword = ''
	while lengthPasswordsInc < lengthPasswords:
			tempPassword += chr(random.randint(33, 125))
			lengthPasswordsInc += 1
	listPasswords += tempPassword + '\n'
	numPasswordsInc += 1
      
print(listPasswords)

\J{=AD8IWIJr"O.R"DD3
K_8M'CWLvv!p)ZON3c?.
iS;v'/A&^tYlObT|_S)\
:kz\cF="[N:EsID$i)YY
.ih3Rl9w1Z2c6'-7=Ss?
9m8},!CB2m<RS$:1I+Iz
&IXj*erS#P{#V;zfF)_3
Teo'#(lF$pK2!?\,'m;o
$ZSc$!t3&C)y]?[^RepB
]qkMpxQTvy-RmDC>7phL


####
while geninc < numPasswords
			passLengthInc = 0
      tempassword = ''
      while passLengthInc < length:
            tem += chr(random.randint(33, 125))
            passLengthInc += 1
      lis += tem + '\n'
      geninc += 1


###
# GENERATE
while geninc < num:
      leninc = 0
      tem = ''
      while leninc < length:
            tem += chr(random.randint(33, 125))
            leninc += 1
      lis += tem + '\n'
      geninc += 1
