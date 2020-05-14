# TODO KILLED ERROR
# CLEANED UP

# for 5 letter words ex 'hello'
string = input()

lisstr = list(string)
lenstr = len(string)

perlis = []
newperlis = []

for x in range(5):
    newperlis.append(lisstr[0])

perlis = newperlis
# this fixed the problem @ 19-21
newperlis = []

# problem here lines 19-21
for idx in range(1,5):
    for prefix in perlis:
        tem = prefix + lisstr[idx]
        newperlis.append(tem)
        #print(newperlis)

perlis = newperlis
newperlis = []

for idx in range(2,5):
    for prefix in perlis:
        tem = prefix + lisstr[idx]
        newperlis.append(tem)
        #print(newperlis)

perlis = newperlis
newperlis = []

for idx in range(3,5):
    for perfix in perlis:
        tem = prefix + lisstr[idx]
        newperlis.append(tem)
        print(newperlis)

perlis = newperlis
newperlis = []

for idx in range(4,5):
    for prefix in perlis:
        tem = prefix + lisstr[idx]
        newperlis.append(tem)

perlis = newperlis
newperlis = []

print(perlis)
print(len(perlis))
