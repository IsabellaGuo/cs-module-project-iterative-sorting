# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # Find the smallest number 
        # move the smallest number to the head
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        
        for j in range (cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        

        # TO-DO: swap
        # Your code here

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # compare first two elements, swap if second is smalled than the first
    # compare the second and the next one, swap if the next is smaller than the first
    for i in range (len(arr)-1):
        for j in range (len(arr)-1-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr




    


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
