from functools import reduce
# def is_even(n):
#     return n%2==0
# def update(n):
#     return n*2
# def add(n,m):
#     return n+m

nums = [1,2,3,6,8,6,9,8]

even = list(filter(lambda n : n%2==0, nums))
doubles = list(map(lambda n : n*2, even))
sum = reduce(lambda n,m: n + m , doubles)
print(even)
print(doubles)
print(sum) 