from  numpy import *

# arr1 = array([
#                 [1,2,3,6,2,9],
#                 [4,5,6,7,5,3]
#            ])
# print(arr1)
# print(arr1.dtype)
# print(arr1.ndim)
# print(arr1.shape)
# print(arr1.size)
# arr2 = arr1.flatten()
#
# print(arr2)
#
# arr3 = arr2.reshape(3,4)
# arr4 = arr3.reshape(2,2,3)
# print(arr3)
# print(arr4)



m1 = matrix('1 2 3; 4 5 6; 7 8 9')
m2 = matrix('9 8 7; 6 5 4; 3 2 1')

m3 = m1 + m2
m4 = m1 - m2
m5 = m1 * m2
m6 = m1 / m2

print(m3)
print(m4)
print(m5)
print(m6)
