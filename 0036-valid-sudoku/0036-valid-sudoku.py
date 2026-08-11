class Solution:
    def isValidSudoku(self, board):
        for i in range(9):
            for j in range(9):
                for k in range(j+1,9):
                    if board[i][j] != "." and board[i][j] == board[i][k]:
                        return False

        for col in range(9):
            for row1 in range(9):
                for row2 in range(row1+1,9):
                    if board[row1][col] != "." and board[row1][col] == board[row2][col]:
                        return False
        
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                cells = []
                for i in range(3):
                    for j in range(3):
                        cells.append(board[box_row+i][box_col+j])
                
                for x in range(9):
                    for y in range(x+1,9):
                        if cells[x] != "." and cells[x] == cells[y]:
                            return False
        
        return True