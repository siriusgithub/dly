str = enter string to parse
chr = enter characters to remove (repeats allowed)
newstr = str

for badchar in chr
    for char in str
        if char == badchar:
           newstr == newstr.replace(badchar,'')

print(newstr)
