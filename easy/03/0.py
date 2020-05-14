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
    ins = (''.join(arr))
    print(''.join(arr))

def enc (msg,inc):
    arr = list(msg)
    for num,let in enumerate(arr):
        arr[num] = encrot(let,inc)
    ins = (''.join(arr))
    print(''.join(arr))

# MAIN
print("Would you like to decrypt (d) or encrypt (e)?")
cry = input()

# DECRYPT
if cry == "d":
   print("\nDo you have a file to decrypt (f) or are you ready to paste the message to decrypt (p)?")
   loc = input()

   # FILE
   if loc == "f":

      # MESSAGE
      print("\nEnter the path to the file: ")
      pat = input()
      infil = open(pat,r)
      msg = infil.read

      # INCREMENT
      print("\nEnter the increment amount: ")
      inc = int(input())
      
      # FUNCTION
      dec(msg,inc)

      # SAVE
      print("\nSave this output in a file (y/n)?")
      sav = input()

      # YES
      if sav == "y":
         print("\nPress enter to save to the current path or give a new path to save to: ")
         out = input()
         print("\nWould you like to write over (w) or append to this file (a)?")
         howfil = input()
         if howfil == "w":
            if out = '':
               
         outfil = open(out,'a')
         outfil.write(ins)
         outfil.close()
   if loc == "p":
      print("\nPaste the message: ")
      msg = input()
      print("\nEnter the increment amount: ")
      inc = int(input())

elif cry == "e":
     print("\nDo you have a file to encrypt (f) or are you ready to paste the message to encrypt (p)?")
     loc = input()
     if loc == "f":
        print("\nEnter the path to the file: ")
        pat = input()
        msg = readfile
        
