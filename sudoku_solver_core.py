from logic import find_empty_cell, is_safe 


# Applying recursive backtracking to solve the Sudoku.
def solve_sudoku(board):

    # TODO 1 : Reaching the Goal State
    find = find_empty_cell(board)
    if not find:
        return True  # True : it have been solved succesfully
    
    row, col = find

    # TODO 2 : Applying the Recursive Loop (or Search algorithm)
    for num in range(1, 10):
        
        # Check if the number is safe (Constraint Check)
        if is_safe(board, num, row, col):
            
    # TODO 3 : Placement and Recursive Call (Go Deeper)
            board[row, col] = num
            
            # If this path leads to a solution, stop and return True
            if solve_sudoku(board):
                return True 

    # TODO 4 : Backtracking 
            # If the recursive call failed, reset the cell and try the next number
            board[row, col] = 0

    # If all numbers (1-9) are tried and failed, backtrack to the previous call
    return False