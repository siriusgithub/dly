print('Calculates primes up to ceiling.')
cei = input('Enter ceiling: ')
cei = int(cei)
prilis = [2]

# problem is because of two for loops
for num in range(2,(cei + 1)):
    print('Num: ' + str(num))
    for pri in prilis:
        if num % pri == 0:
           #print('Modulated by: ' + str(pri))
           break
        else:
            #print('Pri: ' + str(pri))
            print('Appended')
            print('New prilis: ' , end='')
            print(prilis)
            prilis.append(num)
            break

#for num in range(2,(cei + 1)):
#    if num in prilis:

#print(prilis)
print(len(prilis))
