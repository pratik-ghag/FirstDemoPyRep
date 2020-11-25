
names = []
longnames =[]
for i in range(10):
    x = input("Enter a name:")
    names.append(x)
cnt=0
for i in names:


    if len(i)>5:
        longnames.append(i)
        cnt+=1


print(names)
print(longnames)
print("Number of names having more than 5 letters :", cnt)