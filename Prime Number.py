x = 43

for i in range(2, x):
    if x % i == 0:
        print(x, " is Not a Prime Number!")
        break
else:
    print(x, "is a Prime Number!")
