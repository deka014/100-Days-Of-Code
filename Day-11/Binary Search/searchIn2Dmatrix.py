# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

#     Integers in each row are sorted from left to right.
#     The first integer of each row is greater than the last integer of the previous row.

 

# Example 1:

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

 

# Constraints:

#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 100
#     -104 <= matrix[i][j], target <= 104


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        # using binary search 
        
        m = len(matrix[0])
        n = len(matrix)
        
        high = (m*n) - 1
        low = 0
        
        while high >= low : 
            
            mid = (high + low) // 2
            
            if target == matrix[mid//m][mid%m] :
                return True
            
            elif target > matrix[mid//m][mid%m] :
                low = mid + 1
            
            else : 
                high = mid - 1
        
        return False
        
        
# Notes : special technique to find the index of 2d matrix is used
