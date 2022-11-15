# DEFINE -1 = NONE


space_per_squares = 9


# Function to: Check if the guess at the row or column of the puzzle is valid
def validate_guess(sudoku, guess, row, column):
    row_start = (row // 3) * 3
    column_start = (column // 3) * 3
    # Check squares
    for i in range(row_start, row_start + 3):
        for j in range(column_start, column_start + 3):
            if sudoku[i][j] == guess:
                return False

    # Check rows
    rows = sudoku[row]
    if guess in rows:
        return False  # Return false if the guess is repeated

    # Check columns
    cols = [sudoku[i][column] for i in range(space_per_squares)]
    if guess in cols:
        return False  # Return false if the guess is repeated

    return True  # Return true if valid


def find_empty_space(sudoku):
    # finds next row or column that is -1 or empty
    for i in range(space_per_squares):
        for j in range(space_per_squares):
            if sudoku[i][j] == -1:
                return (i, j)
    return (None, None)


def solve(sudoku):
    row, column = find_empty_space(sudoku)

    if row is None or column is None:
        return True

    for i in range(1, 10):
        if validate_guess(sudoku, i, row, column):
            sudoku[row][column] = i
            # Calls solve function recursively
            if solve(sudoku):
                return True
        sudoku[row][column] = -1

    return False  # If the sudoku puzzle is unsolvable


sample_sudoku = [
    [3, 9, -1,   -1, 5, -1,    -1, -1, -1],
    [-1, -1, -1,  2, -1, -1,   -1, -1, 5],
    [-1, -1, -1,  7, 1, 9,     -1, 8, -1],

    [-1, 5, -1,   -1, 6, 8,    -1, -1, -1],
    [2, -1, 6,    -1, -1, 3,   -1, -1, -1],
    [-1, -1, -1,  -1, -1, -1,  -1, -1, 4],

    [5, -1, -1,  -1, -1, -1,   -1, -1, -1],
    [6, 7, -1,    1, -1, 5,      -1, 4, -1],
    [1, -1, 9,   -1, -1, -1,    2, -1, -1]
]


import pprint


print('Sudoku Board : \n')
pprint.pprint(sample_sudoku)
print('\nSolved : \n')
solve(sample_sudoku)
pprint.pprint(sample_sudoku)
