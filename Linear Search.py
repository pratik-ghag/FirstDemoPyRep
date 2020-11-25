pos = 0

def search(list,n):

    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] == i
            return True
        else:
            globals()['pos'] += 1
    return False

list = [5,2,6,9,10,45]
k = 45

if search(list, k):
    print("Found !", pos+1)
else:
    print("Not Found !")

