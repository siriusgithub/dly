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
    
    print(int(n))

nextPerm(38576)

'''
[–]JerMenKoO
 
0 0 2 points 8 years ago* 
You don't need to loop through your list to change everything to number, just use list comprehension:

my_list = [int(x) for x in my_list]
'''
