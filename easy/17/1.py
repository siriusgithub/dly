strparstr = input('Enter string to parse: ')
strremchr = input('Enter characters to remove: ')
newstr = strparstr

for remchr in strremchr:
    for parchr in strparstr:
        if parchr == remchr:
           newstr = newstr.replace(remchr,'')

print(newstr)
