from decimal import Decimal,getcontext

dig = int(input('Digits of pi: '))
getcontext().prec = dig

m = 10

a = [0] * m
b = [0] * m
t = [0] * m
p = [0] * m

one = Decimal(1)
two = Decimal(2)
four = Decimal(4)
half = one / two

a[0] = one
b[0] = (one / two) ** (one / two)
t[0] = one / four
p[0] = one

laspi = 0

for n in range (m-1):
    a[n + 1] = (a[n] + b[n]) / two
    b[n + 1] = (a[n] * b[n]) ** half
    t[n + 1] = t[n] - p[n] * (a[n] - a[n+1]) ** 2
    p[n + 1] = two * p[n]

    pi = (a[n + 1] + b[n + 1]) ** 2 / four/ t[n + 1]
    if laspi == pi:
       break
    laspi = pi

print('Took',n,'Loops')
print('Pi = ',pi)
