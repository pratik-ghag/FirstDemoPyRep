from numpy import *

a1 = array([1, 5, 6, 90])
# shallow copy
# a2 = a1.view()
a2 = a1
#  deep Copy
# a2 = a1.copy()
print(a1)
print(a2)

a1[1] = 22

print(a1)
print(a2)

print(id(a1))
print(id(a2))
