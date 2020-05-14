# TODO REVERSE, MAKE NUMBERS INTO LETTERS
# TODO INTEGRATE EARLIER PHONE NUMBER CHALLENGE TO HAVE CORRECT OUTPUT
pho = input('Enter phone number: ')

outnum = ''
letlis = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

two = ['a','b','c','A','B','C']
thr = ['d','e','f','D','E','F']
fou = ['g','h','i','G','H','I']
fiv = ['j','k','l','J','K','L']
six = ['m','n','o','M','N','O']
sev = ['p','q','r','s','P','Q','R','S']
eig = ['t','u','v','T','U','V']
nin = ['w','x','y','z','W','X','Y','Z']

exclis = ['-','(',')',' ']
numlis = ['1','2','3','4','5','6','7','8','9','0']

for char in pho:
    if char in numlis:
       outnum += char
    elif char in exclis:
         outnum += char
    elif char in letlis:
         if char in two:
            outnum += '2'
         elif char in thr:
              outnum += '3'
         elif char in fou:
              outnum += '4'
         elif char in fiv:
              outnum += '5'
         elif char in six:
              outnum += '6'
         elif char in sev:
              outnum += '7'
         elif char in eig:
              outnum += '8'
         elif char in nin:
              outnum += '9'
    else:
        pass

print(outnum)
