def facto(n):

    if n == 0:
        return 1
    return n * facto(n-1)

result = facto(5)
print(result)