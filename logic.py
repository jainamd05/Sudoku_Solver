import numpy as np

# TODO 1 : we will first find empty spaces

def find_empty_cell(board):
    for x in range(9):
        for y in range(9):
            if board[x , y] == 0:
                return x, y  # Returning the row and column of the empty cell
    return None

# TODO 2 : To have Row Validity Check

def is_valid_row(board, num, row):   
    # to check if a number is placed in the row
    if num in board[row, :]:
        return False
    return True

# TODO 3 : To have Column Validity Check

def is_valid_col(board, num, col):
    # to check if a number is placed in the column
    if num in board[:, col]:
        return False
    return True

# TODO 4 : To have Box Validity Check
# TODO 5 : To have a function that will check wheter the board is valid or not