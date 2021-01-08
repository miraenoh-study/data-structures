# Test the selection sort and the binary search

from random import randint

from selectionsort import sort
import binarysearch
import permutations

MAX_SIZE = 101


# Tests the selection sort
def test_selection_sort():
    # Get the numbers to randomly generate
    print("SELECTION SORT")
    list = []
    n = int(input("Enter the number of numbers to generate: "))
    # Check the value of n
    if n < 1 or n > MAX_SIZE:
        print("Improper value of n")
        raise SystemExit

    # Randomly generate the numbers
    for _ in range(0, n):
        list.append(randint(0, 999))
    # Print the original list
    print("\nOriginal list")
    print(list)

    # Run the selection sort funtion
    list = sort(list, n)

    # Print the sorted list
    print("\nSorted list")
    print(list)

    return list


# Test the loop version binary search
# Get the number to find
def test_binary_search(list, version):
    print("\nBINARY SEARCH", version.upper())
    n = int(input("Enter the number to find: "))

    # Run the binary search function
    if version == "loop":
        index_n = binarysearch.binsearch(list, n)
    elif version == "recursive":
        index_n = binarysearch.binsearch_recursive(list, n, 0, len(list) - 1)
    else:
        print("Invalid version.")
        return

    # Print the search result
    if index_n < 0:
        print("the number doesn't exist in the list.")
    else:
        print("The number's index is", index_n, end="")
        print(".")


# Start the program

# Test the selection sort
list = test_selection_sort()

# Test the binary search
test_binary_search(list, "loop")
test_binary_search(list, "recursive")

# Test the permutaion generator
permutations.generate(['a', 'b', 'c'], 0, 2)
