import numpy as np
#---------------------------------------------------------------------------------------------
# TODO 1 : we will first find empty spaces

def find_empty_cell(board):
    for x in range(9):
        for y in range(9):
            if board[x , y] == 0:
                return x, y  # Returning the row and column of the empty cell
    return None

#---------------------------------------------------------------------------------------------
# TODO 2 : To have Row Validity Check

def is_valid_row(board, num, row):   
    # to check if a number is placed in the row
    if num in board[row, :]:
        return False
    return True

#---------------------------------------------------------------------------------------------
# TODO 3 : To have Column Validity Check

def is_valid_col(board, num, col):
    # to check if a number is placed in the column
    if num in board[:, col]:
        return False
    return True

#---------------------------------------------------------------------------------------------
# TODO 4 : To have Box Validity Check

def is_valid_box(board, num, row, col):
    # to check that there is only one instance of the number in each cube
    cube_r = (row // 3) * 3
    cube_c = (col // 3) * 3
    
    # Using NumPy slicing to extract the 3x3 box
    cube = board[cube_r : ( cube_r + 3 ) , cube_c : ( cube_c + 3 )]

    #  Now to Check if the number is ALREADY in the 3x3 box
    if num in cube :
        return False
    return True

#---------------------------------------------------------------------------------------------
# TODO 5 : To have a function that will check wheter the board is valid or not

def is_safe(board, num, row, col):
    # now combinging all the 3 above checks in bool format
    return (is_valid_row(board, num, row) and
            is_valid_col(board, num, col) and
            is_valid_box(board, num, row, col))