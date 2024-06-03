import random

def generate_sudoku():
    """Generates a solvable Sudoku puzzle."""

    # Create a 9x9 grid filled with 0s
    grid = [[0 for _ in range(9)] for _ in range(9)]

    # Fill the grid with numbers
    fill_grid(grid)

    # Remove some numbers to create a puzzle
    remove_numbers(grid)

    return grid

def fill_grid(grid):
    """Fills the grid with numbers recursively."""

    # Find an empty cell
    empty_cell = find_empty_cell(grid)
    if empty_cell is None:
        return True

    # Try numbers 1-9
    for num in range(1, 10):
        if is_valid(grid, empty_cell, num):
            # Place the number
            grid[empty_cell[0]][empty_cell[1]] = num

            # Recursively fill the rest of the grid
            if fill_grid(grid):
                return True

            # If the number didn't lead to a solution, remove it
            grid[empty_cell[0]][empty_cell[1]] = 0

    # No valid number found
    return False

def find_empty_cell(grid):
    """Finds an empty cell in the grid."""

    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col

    return None

def is_valid(grid, cell, num):
    """Checks if a number is valid at a given cell."""

    row, col = cell

    # Check the row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check the column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check the 3x3 box
    box_row = row // 3
    box_col = col // 3
    for i in range(3):
        for j in range(3):
            if grid[box_row * 3 + i][box_col * 3 + j] == num:
                return False

    return True

def remove_numbers(grid):
    """Removes numbers from the grid to create a puzzle."""

    # Remove 40-50 numbers
    num_to_remove = random.randint(40, 50)
    while num_to_remove > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row][col] != 0:
            grid[row][col] = 0
            num_to_remove -= 1

def print_grid(grid):
    """Prints the grid."""

    for row in grid:
        print(row)

# Generate a Sudoku puzzle
grid = generate_sudoku()

# Print the puzzle
print_grid(grid)