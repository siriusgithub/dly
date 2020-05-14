s="@"
for j in range(int(raw_input("How many lines do you want?"))):
    print s
    s+=s

# reverse
s="@"*(1 << int(raw_input("How many lines?")))
while(s!="@"):
    s=s[:(len(s)/2)]
    print s

'''
the expression (x << y) means "Shift the binary representation of the integer x left by y places, then fill the space to the right with 0s." In arithmetic terms, this very efficiently implements the operation (x * 2y ). For example, 13 << 4 would be 0b1101 with four zeros on the right, so 0b11010000, which is 1324 = 1316=208.
Since I have 1 << n, then I am doing 1*2n, so the integer the expression evaluates to is 2n. Therefore, s is a string of "@" symbols of length 2n.
Since this is python and not C, I probably could have gotten away with 2**int(raw_input()) instead, but old habits die hard I guess.
'''
