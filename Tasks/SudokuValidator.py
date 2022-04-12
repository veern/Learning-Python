import numpy as np

SUDOKU_BOARD_SIZE = 9

def check_row_sum(row, expected):
    return sum(row) == sum(expected)

def valid_solution(board):
    proper_list = range(1,SUDOKU_BOARD_SIZE + 1)
    # Check if row is valid [1,2,...,8,9] (for this scenario)
    for row in board:
        if not check_row_sum(row, proper_list):
            return False
    
    # Check for squares of width = 3 and length = 3 to be valid for sudoku solution (for this scenario)
    N = 0
    increment = int(SUDOKU_BOARD_SIZE / 3) 
    while N + increment < len(board):
        lst = []
        for i in range(N, N+increment):
            for j in range(N, N+increment):
                lst.append(board[i][j])
        if not check_row_sum(lst, proper_list):
            return False
        N += increment

    #rotate whole board to check for valid column
    board = np.array(board, int)
    board = np.rot90(board)
    
    # Check if column is valid [1,2,...,8,9] (for this scenario)
    for row in board:
        if not check_row_sum(row, proper_list):
            return False

            
    return True
        