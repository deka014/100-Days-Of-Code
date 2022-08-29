# 37. Sudoku Solver
# Hard

# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

#     Each of the digits 1-9 must occur exactly once in each row.
#     Each of the digits 1-9 must occur exactly once in each column.
#     Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

# The '.' character indicates empty cells.

 

# Example 1:

# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:


 

# Constraints:

#     board.length == 9
#     board[i].length == 9
#     board[i][j] is a digit or '.'.
#     It is guaranteed that the input board has only one solution.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        n = len(board)
        
        def isSafe(board,row,col,k):
            for i in range(0,9):
                if board[row][i] == str(k):
                    return False
                
                if board[i][col] == str(k):
                    return False
                
                if board[3* (row//3) + i//3][3* (col//3) + i%3] == str(k):
                    return False 
            
            return True
                
                
            
        def solve(board):
            
            for row in range(n):
                for col in range(n):
                    if board[row][col] == ".":
                        
                        for k in range(1,10):
                            
                            if isSafe(board,row,col,k):
                                                              
                                board[row][col] = str(k)

                                if solve(board) == True:
                                    return True

                                board[row][col] = "."
                        
                        return False
                
            return True
        
        solve(board)
        
        
# Note :   if board[3* (row//3) + i//3][3* (col//3) + i%3] == str(k):
#                     return False 

#The above code checks the validity in 3 x 3 sub-grid.
        
        
        