
for j in range(4):
    for i in range(4-j):
        print("# ",end="")

    print()

str1='ABCD'
str2='PQR'
for i in range(4):
     print(str1[ : i+1 ] + str2[ i : ])