nam = input("Enter your name: ")
age = input("Enter your age: ")
use = input("Enter your username for reddit: ")

print("Your name is %s, you are %s years old, and your reddit username is %s." % (nam,age,use))

outfil = open("list1",'a')

ins = "Name: %s\nAge: %s\nUsername: %s\n\n" % (nam,age,use)

outfil.write(ins)
outfil.close()
