strstr = input('Enter string: ')

lisstr = list(strstr)
lenstr = len(strstr)
poslenstr = lenstr

inc = 0
temlis = []

for x in range(poslenstr):
    temlis.append(lisstr[inc])

print(inc)
inc += 1
print(inc)
perlis = temlis
temlis = []

for x in range(poslenstr):
    temlis.append(lisstr[inc])
    inc += 1
    print(inc)

print(temlis)
