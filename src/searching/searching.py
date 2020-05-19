def linear_search(arr, target):
    # Your code here
    # if head value is the target
    for i in range(len(arr)):
        if target == arr[i]:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # set low and high
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        # if midpoint is the target
        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            low = mid + 1
        if arr[mid] > target:
            high = mid - 1

        




    return -1  # not found
 