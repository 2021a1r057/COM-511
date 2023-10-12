def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found the target at index i
    return -1  # Target not found in the list

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Found the target at index mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found in the list

# Example usage:
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 11

# Linear search
linear_result = linear_search(my_list, target)
if linear_result != -1:
    print(f"Linear search: {target} found at index {linear_result}")
else:
    print(f"Linear search: {target} not found in the list")

# Binary search
sorted_list = sorted(my_list)  # Binary search requires a sorted list
binary_result = binary_search(sorted_list, target)
if binary_result != -1:
    print(f"Binary search: {target} found at index {binary_result}")
else:
    print(f"Binary search: {target} not found in the list")
