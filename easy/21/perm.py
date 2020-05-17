from itertools import permutations

def n(numb):
    numb = str(numb)
    for i in sorted(permutations(numb)):
        permutation = int(''.join(i))
        if permutation > int(numb):
           print(permutation)
           break

n(37461)