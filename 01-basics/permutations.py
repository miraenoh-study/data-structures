# Generates all possible permutations of list[i] to list[n]
def generate(list, i, n):
    if i == n:
        for j in range(0, n+1):
            print(list[j], end="")
        print(" ", end="")
    else:
        # list[i] to list[n] has more than one permutation,
        # generate these recursively
        for j in range(i, n+1):
            list[i], list[j] = list[j], list[i]
            generate(list, i+1, n)
            list[i], list[j] = list[j], list[i]