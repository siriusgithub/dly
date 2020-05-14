print('Calculates primes up to ceiling.')
cei = input('Enter ceiling: ')
cei = int(cei)

prilis = [2,3]
inc = 0

for num in range(3,(cei+1)):
    for pri in prilis:
        if num % pri == 0:
           break
        if inc == len(prilis):
           inc = 0
           prilis.append(num)
        else:
            inc += 1




print(prilis)
print(len(prilis))
