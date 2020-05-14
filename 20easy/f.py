print('Program finds primes up to ceiling.')
cei = input('Enter ceiling: ')
cei = int(cei)

prilis = [2]

for num in range(2,(cei+1)):
    inc = 0
    for pri in prilis:
        if num % pri == 0:
           break
        if num % pri != 0:
           inc += 1
        if inc == len(prilis):
           prilis.append(num)
           break

prilis.insert(0,1)

print(prilis)
print(len(prilis))
