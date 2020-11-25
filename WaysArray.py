from numpy import *
# Normal typ of array
arr1 = array([10,25,26,49],float)
print(arr1)
#  (start , end, parts(50 by default))
arr2 = linspace(1,10,5)
print(arr2)
#  (start , end, parts(not specific))
arr3 = logspace(1,20,7)
print(arr3)
# like range
arr4 = arange(1,25,3)
print(arr4)
#  all elements will be default 0's need to specify size
arr5 = zeros(7)
print(arr5)
#  all elements will be default 1's need to specify size
arr6 = ones(8)
print(arr6)