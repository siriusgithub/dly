import hashlib

lis = ['12345','54321','hovroc','l%Hovroc13']

for num,pas in enumerate(lis):
    pas = pas.encode('utf-8')
    haspas = hashlib.sha512(pas).hexdigest()
    print(haspas)

'''
    tem = lis[num]
    tem = tem.encode('utf-8')
    pas = hashlib.sha512(tem).hexdigest()
    print(pas)
    num += 1
'''

#lookup = 'perce\n'
#
#with open('list') as myFile:
#     for num, line in enumerate(myFile, 1):
#         if lookup in line:
#            print('found at line:', num)
#
#print(lis.index("hovroc"))
