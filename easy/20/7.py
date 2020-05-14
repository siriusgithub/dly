inc = 0
prilis = [2]

for num in range(2,2000):
    inc = 0
    for pri in prilis:
        if num % pri == 0:
           break
        if num % pri != 0:
           inc += 1
        if inc == len(prilis):
           prilis.append(num)
           break


print(prilis)
print(len(prilis))
