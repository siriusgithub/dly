def triangle(height):
line = '@'
x= 1
if height == 0:
    print('Triangle of height 0 not valid!')
while x <= height:
    print(line)
    line *= 2
    x+=1

def reversetriangle(height):
line = '@'
x= height
if height == 0:
    print('Triangle of height 0 not valid!')
while x > 0:
    line = '@'*2**(x-1)
    print('{:>70}'.format(line))
    x-=1
