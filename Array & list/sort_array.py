from array import *
arr = array('i', [8, 7, 6, 45, 1, 82, 61, 2, 3, 12])

# selection sort
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp


for i in range(len(arr)):
    print(arr[i], end=" ")
