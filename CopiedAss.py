# //10 Names from user
from array import *
arr=[]
n=10
for i in range(n):
    x=input("enter the name")
    arr.append(x)
print(arr)
# //Count and display the names with length more than 5
cnt=0
for j in (arr):
    if(len(j)>5):
        print("name:{},length:{}".format(j,len(j)))
        cnt+=1
print("Total number of names with length more than 5 is:" ,cnt)