import numpy as np

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
print_board(initial_board)