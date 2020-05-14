print('Calculates primes up to ceiling.')
cei = input('Enter ceiling: ')
cei = int(cei)

prilis = [2]
temlis = []

for num in range(2,(cei + 1)):
    don = False
    for pri in prilis:
        if num % pri == 0:
           temlis.append(num)
        if len(temlis) == len(prilis):
           prilis.append(num)
           break


print(prilis)
print(len(prilis))

for x in xrange(10):
    for y in xrange(10):
        for z in xrange(10):
            print x,y,z
            if x*y*z == 30:
                break
        else:
            continue
        break
    else:
        continue
    break
