from math import sqrt

n = 43

for i in range(2, int(sqrt(n) + 1)):

    if n % i == 0:
        print(n, ' is not prime, can be divisible by :', i)
        break
else:
    print(n, ' is prime number')