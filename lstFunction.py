lst = []
le = int(input('Enter the size of list'))


for i in range(le):
    x = int(input("Enter next Elemnet"))
    lst.append(x)

def count(*data):
    even = 0
    odd = 0

    for e in lst:
        if e%2==0:
            even+=1
        else:
            odd+=1
    return even, odd

even, odd = count(lst)
print(lst)
print("Even : {} and Odd : {}".format(even,odd))