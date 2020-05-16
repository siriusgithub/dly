def nextPerm(n):
r = False
n = list(str(n))
for i in range(len(n)):
    n[i] = int(n[i])
n.reverse()
for i in range(len(n)):
    for j in range(len(n)-i):
        if n[i] > n[j]:
            n.insert(j+1, n[i])
            n.pop(i)
            r = True
            break
    if r:
        break
n.reverse()
n = ''.join(map(str, n))
return int(n)

unsortedList = [46588	,77086,	53762,	52614	,16237]

for number in unsortedList:
   nextPerm(number)