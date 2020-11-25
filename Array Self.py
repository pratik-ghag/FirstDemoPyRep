from array import *

arr = array('i',[])

asize=int(input('Enter the size of array: '))

for i in range(asize):
     val = int(input('Enter the next Element: '))
     arr.append(val)

print(arr)

afind = int(input('Enter Element to search:'))

k=0
for e in arr:
    if e == afind:
        print(k)
        break
    k+=1

print(arr.index(afind))
    

