# 51. N-Queens
# Hard

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

# Example 1:

# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Example 2:

# Input: n = 1
# Output: [["Q"]]

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        output = []
        
        board = [["." for i in range(n)] for i in range(n)]
        
        def isSafe(board,row,col):
            for i in range(col,-1,-1):
                if board[row][i] == "Q":
                    return False
                
            for i , j in zip(range(row,-1,-1),range(col,-1,-1)):
                if board[i][j] == "Q":
                    return False
            
            for i , j in zip(range(row,n),range(col,-1,-1)):
                if board[i][j] == "Q":
                    return False
            return True
        
        def solve(board,col):
            
            
            if col == n :
                # //in 2d array we need to make a deepcopy like below
                output.append([row[:] for row in board])
                return
            
            for row in range(n):
                if not isSafe(board,row,col):
                    continue
                    
                board[row][col] = "Q"
                
               
                solve(board,col+1)
                
                board[row][col] = "."
        
        solve(board,0)
        
        result = []
        
        for i in output:
            temp = []
            for j in i:
                
                temp.append("".join(j))
            result.append(temp)
        
        return result
            
        
