# TODO INCOPORATE LADDER BREAKS AND CONTINUES, SEE https://stackoverflow.com/questions/653509/breaking-out-of-nested-loops OR USE RETURN

print('Calculates primes up to ceiling.')
cei = input('Enter ceiling: ')
cei = int(cei)

prilis = [2]
temlis = []

for num in range(3,(cei + 1)):
    for pri in prilis:
        if num % pri == 0:
           temlis.append(pri)
           break
        else:
            prilis.append(num)
            continue
        break
    else:
        continue

print(prilis)
print(len(prilis))
