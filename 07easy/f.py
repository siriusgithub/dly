# add beeping of the message out then and there or save the beeping into a sound file/movie
# add tapping of spacebar when entering in morse code

# MAIN
# EXPLANATION
print('\nMorse code converter/deconverter with spaces represented as " / " and spaces between each morse letter,\n')

# OPTION
print('Convert text to morse code (m) or convert morse code to text (t)?')
opt = input()

# TO MORSE
if opt == 'm':

   # INPUT
   print('\nEnter string:')
   string = input()
   arr = list(string)

   # CONVERSION
   for num,let in enumerate(arr):
       if let == 'a' or let == 'A':
          arr[num] = '.- '
       elif let == 'b' or let == 'B':
            arr[num] = '-... '
       elif let == 'c' or let == 'C':
            arr[num] = '-.-. '
       elif let == 'd' or let == 'D':
            arr[num] = '-.. '
       elif let == 'e' or let == 'E':
            arr[num] = '. '
       elif let == 'f' or let == 'F':
            arr[num] = '..-. '
       elif let == 'g' or let == 'G':
            arr[num] = '--. '
       elif let == 'h' or let == 'H':
            arr[num] = '.... '
       elif let == 'i' or let == 'I':
            arr[num] = '.. '
       elif let == 'j' or let == 'J':
            arr[num] = '.--- '
       elif let == 'k' or let == 'K':
            arr[num] = '-.- '
       elif let == 'l' or let == 'L':
            arr[num] = '.-.. '
       elif let == 'm' or let == 'M':
            arr[num] = '-- '
       elif let == 'n' or let == 'N':
            arr[num] = '-. '
       elif let == 'o' or let == 'O':
            arr[num] = '--- '
       elif let == 'p' or let == 'P':
            arr[num] = '.--. '
       elif let == 'q' or let == 'Q':
            arr[num] = '--.- '
       elif let == 'r' or let == 'R':
            arr[num] = '.-. '
       elif let == 's' or let == 'S':
            arr[num] = '... '
       elif let == 't' or let == 'T':
            arr[num] = '- '
       elif let == 'u' or let == 'U':
            arr[num] = '..- '
       elif let == 'v' or let == 'V':
            arr[num] = '...- '
       elif let == 'w' or let == 'W':
            arr[num] = '.-- '
       elif let == 'x' or let == 'X':
            arr[num] = '-..- '
       elif let == 'y' or let == 'Y':
            arr[num] = '-.-- '
       elif let == 'z' or let == 'Z':
            arr[num] = '--.. '
       elif let == ' ':
            arr[num] = '/ '
       else:
           arr[num] = arr[num]

       # OUTPUT
       out = ''.join(arr)

   # PRINT MORSE
   print('\n')
   print(out)

# FROM MORSE
elif opt == 't':

     # INPUT
     print('Enter morse code:')
     morse = input()
     arr = morse.split(' ')

     # CONVERSION
     for num,let in enumerate(arr):
         if let == '.-':
            arr[num] = 'A'
         elif let == '-...':
              arr[num] = 'B'
         elif let == '-.-.':
              arr[num] = 'C'
         elif let == '-..':
              arr[num] = 'D'
         elif let == '.':
              arr[num] = 'E'
         elif let == '..-.':
              arr[num] = 'F'
         elif let == '--.':
              arr[num] = 'G'
         elif let == '....':
              arr[num] = 'H'
         elif let == '..':
              arr[num] = 'I'
         elif let == '.---':
              arr[num] = 'J'
         elif let == '-.-':
              arr[num] = 'K'
         elif let == '.-..':
              arr[num] = 'L'
         elif let == '--':
              arr[num] = 'M'
         elif let == '-.':
              arr[num] = 'N'
         elif let == '---':
              arr[num] = 'O'
         elif let == '.--.':
              arr[num] = 'P'
         elif let == '--.-':
              arr[num] = 'Q'
         elif let == '.-.':
              arr[num] = 'R'
         elif let == '...':
              arr[num] = 'S'
         elif let == '-':
              arr[num] = 'T'
         elif let == '..-':
              arr[num] = 'U'
         elif let == '...-':
              arr[num] = 'V'
         elif let == '.--':
              arr[num] = 'W'
         elif let == '-..-':
              arr[num] = 'X'
         elif let == '-.--':
              arr[num] = 'Y'
         elif let == '--..':
              arr[num] = 'Z'
         elif let == '/':
              arr[num] = ' '

         # OUTPUT
         out = ''.join(arr)

     # PRINT STRING
     print('\n')
     print(out)
