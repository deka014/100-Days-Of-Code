class Solution:
    def isValidSudoku(self, board) :
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        squareSet = [[set() for _ in range(3)]for y in range(3)]


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in rowSet[i] or board[i][j] in colSet[j] or board[i][j] in squareSet[i//3][j//3]):
                    print("wow")
                    return False
                colSet[j].add(board[i][j])
                rowSet[i].add(board[i][j])
                squareSet[i//3][j//3].add(board[i][j])
            
        return True

           

# 36. Valid Sudoku
# Medium
# 9K
# 939
# Companies

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:

#     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.

 

# Example 1:

# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

        
                
