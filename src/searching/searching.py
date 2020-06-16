def linear_search(arr, target):
    # Your code here
    for i in arr:
        if i == target:
            return arr.index(i)
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    middle_index = (len(arr) // 2) - 1
    current = middle_index
    while current > 0 and current < len(arr)-1:
        if target == arr[current]:
            return current
        elif target < arr[current]:
            current -= 1
        elif target > arr[current]:
            current += 1
    return -1  # not found
