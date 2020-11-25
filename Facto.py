

def facto(x):

    f = 1
    for i in range(1,x+1):
        f = f * i

    return f

x = int(input("ENter a Number: "))
result = facto(x)
print(result)
