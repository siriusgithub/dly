import string, sys
table = string.maketrans(string.ascii_letters, '22233344455566677778889999' * 2)
basic = sys.argv[1].translate(table, '-')
print '{0}-{1}-{2}-{3}'.format(basic[0], basic[1:4], basic[4:7], basic[7:])
