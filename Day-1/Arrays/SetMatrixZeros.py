# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's
# Example 1:

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        
        rowArr = [-1 for i in range(row)]
        colArr = [-1 for i in range(col)]
        
        for i in range(row):
            for j in range(col):
                
                if matrix[i][j] == 0:
                    rowArr[i] = 0
                    colArr[j] = 0
        
        for i in range(row):
            for j in range(col):      
                
                if rowArr[i] == 0 or colArr[j] == 0:
                    matrix[i][j] = 0
            
                    
                    
                
                
                