numlis = []

for num in range(100):
    numlis.append(num)

# If break is commented out the len of numlis is 50
for num in numlis:
    if num % 2 == 0:
       numlis.remove(num)
       break

print(numlis)
print(len(numlis))
