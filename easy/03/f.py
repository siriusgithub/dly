# currently working on save functionality

# FUNCTIONS
def decrot (let,inc):
    num = ord(let)
    if num >= ord('a') and num <= ord('z'):
       return chr(ord('a') + (num-ord('a') - inc) % 26)
    if num >= ord('A') and num <= ord('Z'):
       return chr(ord('A') + (num-ord('a') - inc) % 26)
    return let

def encrot (let,inc):
    num = ord(let)
    if num >= ord('a') and num <= ord('z'):
       return chr(ord('a') + (num-ord('a') + inc) % 26)
    if num >= ord('A') and num <= ord('Z'):
       return chr(ord('A') + (num-ord('a') + inc) % 26)
    return let

def dec (msg,inc):
    arr = list(msg)
    for num,let in enumerate(arr):
        arr[num] = decrot(let,inc)
    out = (''.join(arr))
    print(''.join(arr))

def enc (msg,inc):
    arr = list(msg)
    for num,let in enumerate(arr):
        arr[num] = encrot(let,inc)
    out = (''.join(arr))
    print(''.join(arr))

# MAIN
print("Would you like to decrypt (d) or encrypt (e)?")
cry = input()

# DECRYPT
if cry == 'd':

   # FILE OR PASTE
   print("\nDo you have a file (f) or a message to input (i)?")
   typ = input()

   # FILE
   if typ == 'f':

      # MESSAGE
      print("\nEnter the path to the file: ")
      pat = input()

      infil = open(pat,'r')
      msg = infil.read

      # INCREMENT
      print("\nEnter the decrement amount: ")
      decrem = int(input())

      # FUNCTION
      dec(msg,decrem)

      # SAVE
      print("\nSave this output to a file (y/n)?")
      sav = input()

      # YES
      if sav == 'y':
         print("\nPress enter to save to the read path or give a new path: ")
         savpat = input()

         # ADD OR REWRITE
         print("\nWould you like to write over this file (w) or append to it (a)?")
         wri = input()

         # REWRITE
         if wri == 'w':
            if savfil == '':
               infil.close()
               outfil = open(pat,'w')
               outfil.write(out)
               outfil.close()
            else:
                infil.close()
                outfil = open(savpat,'w')
                outfil.write(out)
                outfil.close()

         elif wri == 'a':
              if savfil == '':
                 infil.close()
                 outfil = open(pat,'a')
                 outfil.write(out)
                 outfil.close()
              else:
                  infil.close()
                  outfil = open(pat,'a')
                  outfil.write(out)
                  outfil.close()

      # NO
      elif sav == 'n':
           quit()
                

   # PASTE
   elif typ == 'i':

        # MESSAGE
        print("\nPaste/type the message: ")
        msg = input()

        # INCREMENT
        print("\nEnter the decrement amount: ")
        decrem = int(input())

        # FUNCTION
        dec(msg,decrem)

        # SAVE 
        print("\nSave this output to a file (y/n)?")
        sav = input()

        # YES
        if sav == 'y':
           print("\nPress enter to save to the read path or give a new path: ")
           savpat = input()

           # ADD OR REWRITE
           print("\nWould you like to write over this file (w) or append to it (a)?")
           wri = input()

           # REWRITE
           if wri == 'w':
              if savpat == '':
                 infil.close()
                 outfil = open(pat,'w')
                 outfil.write(out)
                 outfil.close()
              else:
                  infil.close()
                  outfil = open(savpat,'w')
                  outfil.write(out)
                  outfil.close()

           elif wri == 'a':
                if savpat == '':
                   infil.close()
                   outfil = open(pat,'a')
                   outfil.write(out)
                   outfil.close()
                else:
                    infil.close()
                    outfil = open(pat,'a')
                    outfil.write(out)
                    outfil.close()

        # NO
        elif sav == 'n':
             quit()

# ENCRYPT
elif cry == 'e':

     # FILE OR PASTE
     print("\nDo you have a file (f) or a message to input (i)?")
     typ = input()

     # FILE
     if typ == 'f':

        # MESSAGE
        print("\nEnter the path to the file: ")
        pat = input()

        infil = open(pat,'r')
        msg = infil.read

        # INCREMENT
        print("\nEnter the increment amount: ")
        inc = int(input())

        # FUNCTION
        enc(msg,inc)

        # SAVE
        print("\nSave this output to a file (y/n)?")
        sav = input()

        # YES
        if sav == 'y':
           print("\nPress enter to save to the read path or give a new path: ")
           savpat = input()

           # ADD OR REWRITE
           print("\nWould you like to write over this file (w) or append to it (a)?")
           wri = input()

           # REWRITE
           if wri == 'w':
              if savfil == 'o':
                 infil.close()
                 outfil = open(pat,'w')
                 outfil.write(out)
                 outfil.close()
              else:
                  infil.close()
                  outfil = open(savpat,'w')
                  outfil.write(out)
                  outfil.close()

           elif wri == 'a':
                if savfil == '':
                   infil.close()
                   outfil = open(pat,'a')
                   outfil.write(out)
                   outfil.close()
                else:
                    infil.close()
                    outfil = open(pat,'a')
                    outfil.write(out)
                    outfil.close()

        # NO
        elif sav == 'n':
             quit()

     # PASTE
     elif typ == 'i':

          # MESSAGE
          print("\nPaste/type the message: ")
          msg = input()

          # INCREMENT
          print("\nEnter the increment amount: ")
          inc = int(input())

          # FUNCTION
          enc(msg,inc)

          # SAVE
          print("\nSave this output to a file (y/n)?")
          sav = input()

          # YES
          if sav == 'y':
             print("\nPress enter to save to the read path or give a new path: ")
             savpat = input()

             # ADD OR REWRITE
             print("\nWould you like to write over this file (w) or append to it (a)?")
             wri = input()
  
             # REWRITE
             if wri == 'w':
                if savfil == '':
                   infil.close()
                   outfil = open(pat,'w')
                   outfil.write(out)
                   outfil.close()
                else:
                    infil.close()
                    outfil = open(savpat,'w')
                    outfil.write(out)
                    outfil.close()

             elif wri == 'a':
                  if savfil == '':
                     infil.close()
                     outfil = open(pat,'a')
                     outfil.write(out)
                     outfil.close()
                  else:
                      infil.close()
                      outfil = open(pat,'a')
                      outfil.write(out)
                      outfil.close()

          # NO
          elif sav == 'n':
               quit()
