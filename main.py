import numpy as np
import matplotlib.pyplot as plt 
from logic import find_empty_cell, is_safe
from sudoku_solver_core import solve_sudoku

# creating a 9x9 numpy array to represent a Sudoku board
initial_board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])


print("Initial Sudoku Board :\n")
print(initial_board)

# To visualize the board in a better format
def print_board(board):

    print("\n+-------+-------+-------+")     # After every cube section

    for i in range(len(board)):
        # To print an horizontal line after every cube
        if i % 3 == 0 and i != 0:
            print("|-------+-------+-------|")
        
        for j in range(len(board[0])):
            # Print a vertical line before every cube
            if j % 3 == 0:
                print("| ", end="")

            print(board[i][j] if board[i][j] != 0 else ".", end=" ")     # To print empty space with a dot(.)

            if j == 8:
                print("|")
    print("+-------+-------+-------+")

# Trying is it working correctly 
print("\nFormatted Sudoku Board :")
print_board(initial_board)

"""Some test cases to check wheter the functions are working correctly or not"""
# Test 1: Finding an empty cell
empty_pos = find_empty_cell(initial_board)
print(f"Empty cell at : {empty_pos}")
# Test 2: Is placing '5' at (0, 2) safe? (Should be False, as '5' is in row 0)
is_5_safe = is_safe(initial_board, 5, 0, 2)
print(" Is 5 safe ? " , is_5_safe)


solvable_board = initial_board.copy() # Making a copy to preserve the original board

# Function to Visualize the Solved Board
def visualize_board(original, solved):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(solved, cmap='binary', interpolation='nearest') 
    # Draw grid lines for 3x3 boxes
    for x in range(0, 10, 3):
        ax.axhline(x - 0.5, color='black', linewidth=3)
        ax.axvline(x - 0.5, color='black', linewidth=3)
        
    for x in range(0, 10):
        ax.axhline(x - 0.5, color='gray', linewidth=1)
        ax.axvline(x - 0.5, color='gray', linewidth=1)
    for r in range(9):
        for c in range(9):
            num = solved[r, c]
            if num != 0:
                color = 'black' if original[r, c] != 0 else 'blue'
                ax.text(c, r, str(num), va='center', ha='center', fontsize=20, color=color)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Sudoku Solver Visualization", fontsize=16)
    plt.show()
if solve_sudoku(solvable_board):
    visualize_board(initial_board, solvable_board) # Visualize the solved board

# Solving the Sudoku
if solve_sudoku(solvable_board):
    print("\nSudoku Solved Successfully!\n")
    print_board(solvable_board)
else:
    print("\nERROR: No solution exists for this Sudoku puzzle.")