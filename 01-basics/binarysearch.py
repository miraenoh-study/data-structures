# Binary search functions using loop or recursive structure

# Performs the binary search
# Loop version
def binsearch(list, searchnum):
    # The index of the first element
    left = 0
    # The index of the last element
    right = len(list) - 1

    # Perform the binary search
    while left <= right:
        middle = (left + right) // 2
        if searchnum < list[middle]:
            right = middle - 1
        elif searchnum > list[middle]:
            left = middle + 1
        else:
            # Found the number
            return middle

    # Failed to find the number
    return -1


# Performs the binary search
# Recursive version
def binsearch_recursive(list, searchnum, left, right):
    if left <= right:
        middle = (left + right) // 2
        if searchnum < list[middle]:
            return binsearch_recursive(list, searchnum, left, middle - 1)
        elif searchnum > list[middle]:
            return binsearch_recursive(list, searchnum, middle + 1, right)
        else:
            # Found the number
            return middle

    # Failed to find the number
    return -1
