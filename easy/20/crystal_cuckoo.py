def eratosthenes(n):
    A = [True]*(n+1)
    for i in range(2, int(n/2)+1):
        if A[i]:
            for j in range(2*i, n+1, i):
                A[j] = False
    return [i for i in range(2, n+1) if A[i]]

print(eratosthenes(1000000))
