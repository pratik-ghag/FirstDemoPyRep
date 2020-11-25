from array import *

vals = array('i', [6, 78, 25, 9])

for i in vals:
    print(i)

newarr = array(vals.typecode, (a*a for a in vals))

for e in newarr:
    print(e)

i=0
while i<len(vals):
    print(vals[i])
    i+=1