#better runtime
def removeCharFromStr(str, index):
    endIndex = index if index == len(str) else index + 1
    return str[:index] + str[endIndex:]

# 'ab' -> a + 'b', b + 'a'
# 'abc' ->  a + bc, b + ac, c + ab
#           a + cb, b + ca, c + ba
def perm(str):
    if len(str) <= 1:
        return {str}
    permSet = set()
    for i, c in enumerate(str):
        newStr = removeCharFromStr(str, i)
        retSet = perm(newStr)
        for elem in retSet:
            permSet.add(c + elem)
    return permSet
