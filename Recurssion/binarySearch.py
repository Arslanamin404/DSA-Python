# Recursive Approach
# TODO: BINARY SEARCH Algorithm
# * Note: Array Must be Sorted

def binary_search(arr, target, left, right):
    if left > right:
        return False

    mid = (left+right)//2

    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, right)
    else:
        return binary_search(arr, target, left, mid-1)


if __name__ == "__main__":
    myList = [10, 2, 89, 25, 6, 69, 9, 1]
    myList.sort()
    print(myList)

    left = 0
    right = len(myList)-1

    target = 1

    if binary_search(myList, target, left, right):
        print(f"Target Found!")
    else:
        print("Target Not Found!")
