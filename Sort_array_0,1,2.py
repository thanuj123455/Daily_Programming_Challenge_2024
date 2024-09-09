
def sort_array(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr
# TEST CASES
# Test Case 1
print(sort_array([0, 1, 2, 1, 0, 2, 1, 0])) 
# Test Case 2
print(sort_array([2, 2, 2, 2])) 

# Test Case 3
print(sort_array([0, 0, 0, 0])) 
# Test Case 4
print(sort_array([1, 1, 1, 1]))  
# Test Case 5
print(sort_array([2, 0, 1])) 

# Test Case 6
print(sort_array([]))  
