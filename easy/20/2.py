print('Calculates primes up to ceiling.')
cei = input('Enter ceiling: ')
cei = int(cei)
prilis = [1,2,3,5,7,11,13]

for num in range(2,(cei + 1)):
    for pri in prilis:
        if num % pri == 0:
           pass
        elif num % pri != 0:
             prilis.append(num)

print(prilis)
print(len(prilis))
