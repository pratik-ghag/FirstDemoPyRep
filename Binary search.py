pos = -1


def search(lst, n):

    l = 0
    u = len(lst)

    while l <= u:
        mid = (l+u) // 2

        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < n:
                l = mid + 1
            else:
                u = mid - 1


    return False


lst = [5, 2, 6, 9, 10, 45]
k = 5
list.sort(lst)

if search(lst, k):
    print("Found !", pos+1)
else:
    print("Not Found !")

