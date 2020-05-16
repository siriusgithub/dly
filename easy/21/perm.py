from itertools import permutations

def n():
    numb = input('Enter your number: ')
    for i in sorted(permutations(numb)):
        permutation = int(''.join(i))
        if permutation > int(numb):
           print(permutation)
           break

n()
