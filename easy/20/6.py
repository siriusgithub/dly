print('Calculates primes up to ceiling.')                                                                             
cei = input('Enter ceiling: ')
cei = int(cei)

prilis = [2]
 
for num in range(2,(cei + 1)):
    inc = 0
    prilislen = len(prilis)
    while inc != prilislen:
          for pri in prilis:
              if num % pri == 0:
                 temlis.append(num)

