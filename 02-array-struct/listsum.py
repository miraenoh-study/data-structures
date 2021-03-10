# Returns the sum of an input array's elements
def sum(list):
    tempsum = 0
    # Add each element into tempsum
    for el in list:
        tempsum += el

    return tempsum


# Test the sum function
input = [1, 2, 3, 4]
answer = sum(input)

print("The sum is:", answer)
print(input)
