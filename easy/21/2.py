print('Find next prime using same digits of given number.')
strnum = input('Enter number: ')

diglis = []

for pos in strnum:
    diglis.append(int(pos))

revdiglis = list(reversed(diglis))

print(diglis)
print(revdiglis)

pre = 0
cur = 0

for pos in revdiglis:
    if pre == pos:
