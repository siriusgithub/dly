def rot_char(c,d):
    num = ord(c)
    if num >= ord('a') and num <= ord('z'):
        return chr(ord('a') + (num-ord('a')+d)%26)
    if num >= ord('A') and num <= ord('Z'):
        return chr(ord('A') + (num-ord('a')+d)%26)
    return c

def rot(msg,d=13):
    arr = list(msg)
    for i,c in enumerate(arr):
        arr[i] = rot_char(c,d)
    print( ''.join(arr))

rot("hello there",24)
