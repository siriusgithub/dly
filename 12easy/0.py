# for 5 letter words ex 'hello'
string = input()

lisstr = list(string)
lenstr = len(string)

perlis = []
#for idx in range(lenstr):
#    for idx in range(5):
#        perlis.append(lisstr[0])
#        print(perlis)
       # for x in range(4):
       #     for idx in range(1,5):
       #         for prefix in perlis:
       #             prefix + string[idx]
       #             for x in range(3):
       #                 for idx in range(2,5):
       #                     for prefix in perlis:
       #                         prefix + string[idx]
       #                         for x in range(2):
       #                             for idx in range(3,5):
       #                                 for prefix in perlis:
       #                                     prefix + string[idx]
       #                                     for x in range(1):
       #                                         for idx in range(4,5):
       #                                             for prefix in perlis:
newperlis = []
       #                                                 prefix + string[idx]

for x in range(5):
    newperlis.append(lisstr[0])

perlis = newperlis

for idx in range(1,5):
    for prefix in perlis:
        tem = prefix + lisstr[idx]
        newperlis.append(tem)

perlis = newperlis

#for idx in range(2,5):
#    for prefix in perlis:
#        tem = prefix + lisstr[idx]
#        newperlis.append(tem)
#
#perlis = newperlis
#
#for idx in range(3,5):
#    for perfix in perlis:
#        tem = prefix + lisstr[idx]
#        newperlis.append(tem)
#
#perlis = newperlis
#
#for idx in range(4,5):
#    for prefix in perlis:
#        tem = prefix + lisstr[idx]
#        newperlis.append(tem)
#
perlis = newperlis

print(perlis)
print(len(perlis))

#for item in perlis:
#    print(item)


#            [prefix + string[idx] for prefix in perlis]


##########################
#enter string
#
#convert string into list of letters
#
#for each letter
#    
