# https://www.reddit.com/r/dailyprogrammer/comments/qr0hg/3102012_challenge_22_easy/

'''
Write a program that will compare two lists, and append any elements in the second list that doesn't exist in the first.

input: ["a","b","c",1,4,], ["a", "x", 34, "4"]

output: ["a", "b", "c",1,4,"x",34, "4"]
'''

# to specify number strings ' or " must be used 
# spaces indicate a seperation of items
# strings can be put in quotest to have sentences

# 1
def append_unique(a, b):
    return a + [item for item in b if item not in a]

# 2
def append_set(a, b):
    p_set = a[:]
    for c in b:
        if c not in a:
            p_set.append(c)
    return p_set 

append_set(['a', 'b', 'c', 1, 4], ['a', 'x', 34, '4'])

# 3
def mixer(list1,list2):
    for item in list2:
        if item not in list1:
            list1.append(item)
    return list1

# 4
a, b = ["a","b","c",1,4], ["a", "x", 34, "4"]
c = set(a+b)

# 5
list_union = lambda x, y: list(set(x).union(y))

# 6
def merge(a, b):
    for item in b:
        if item not in a:
            a.append(item)
    return a

# 7
a = input()
b = input()
c = [] + a
for i in b:
    if i not in c:
        c.append(i)

# 8
list_1=["a","b","c",1,4]
list_2=["a", "x", 34, "4"]
list_3= list_1+list_2
for x in list_3:
    if list_3.count(x)>1:
        list_3.remove(x)

print list_3