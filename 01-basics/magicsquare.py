# Magic square with odd size

# Generates the magic square iteratively
def generate(size):
    # Check if the size is not wrong
    if size < 1 or not size % 2:
        print("Size is out of range")
        raise SystemExit

    # Initiate the magic square to generate with zeros
    square = [[0 for col in range(size)] for row in range(size)]

    # row, col: current position
    row = 0
    col = size // 2

    # First, put 1 on the middle of the first row
    square[row][col] = 1

    # Diagonally move up left adding 1
    for count in range(2, size ** 2 + 1):
        # Move up
        new_row = row - 1 if row > 0 else size - 1
        # Move left
        new_col = col - 1 if col > 0 else size - 1

        # If the cell has been already filled, move down
        if square[new_row][new_col]:
            row = row + 1
        else:
            # The cell is empty
            row = new_row
            col = new_col

        # Fill the cell
        square[row][col] = count

    return square


# Test the generate function
# Get the user input and call the generate function with it
size = int(input("Enter the size of the square: "))
square = generate(size)

# Print the result
for row in square:
    for col in row:
        print(col, end="\t")
    print()
