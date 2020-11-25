from array import *
# //creating an empty array
arr = array('i', [])
# asking array size from user
asize = int(input('Enter the size of array:'))

for i in range(asize):
    val = int(input("Enter the next Element:"))
    arr.append(val)

print(arr)

val1 = int(input('Enter the value for search:'))

k = 0
for e in arr:
    if e == val1:
        print(k)
        break
    k+=1
print(arr.index(val1))
