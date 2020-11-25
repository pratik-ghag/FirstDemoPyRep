def fibo(n):
    a = 0
    b = 1
    if n <= 0:
        print("invalid value enter a valid one!")
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)
        c = 0
        for i in range(n):
            c = a + b
            if c > n:
                break
            print(c)
            a = b
            b = c
x = int(input("enter till how many numbers you want fibonacci series = "))
fibo(x)