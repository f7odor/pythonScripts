def binarySearch(mylist, find, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if find == mylist[mid]:
            return mid
        elif find < mylist[mid]:
            return binarySearch(mylist, find, 0, mid-1)
        else:
            return binarySearch(mylist, find, mid + 1, stop)

mylist = [10, 12, 13, 15, 25, 26, 28, 33, 42, 44, 46, 50]
find = 14

x = binarySearch(mylist, find, 0, len(mylist))

if x == False:
    print("Item ", find, "Not Found!")
else:
    print("Item ", find, "Found at Index ", x)
