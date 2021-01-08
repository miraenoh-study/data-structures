# Selection sort

# Performs the selection sort
def sort(list, n):
    # For each list index except the last one
    for i in range(0, n-1):
        # Find the proper value for the index
        min = i
        for j in range(i+1, n):
            if list[j] < list[min]:
                min = j

        # Relocate the proper value
        list[i], list[min] = list[min], list[i]

    return list
