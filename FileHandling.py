f1 = open('abc', 'r')
f2 = open('abbc', 'w')

for data in f1:
    f2.write(data)