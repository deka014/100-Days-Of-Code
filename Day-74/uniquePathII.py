# 63. Unique Paths II
# Medium
# 7.9K
# 470
# Companies

# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:

# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

# Example 2:

# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1

 

# Constraints:

#     m == obstacleGrid.length
#     n == obstacleGrid[i].length
#     1 <= m, n <= 100
#     obstacleGrid[i][j] is 0 or 1.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 :
            return 0

        if m==0 or n==0 :
            return 0

        path =  [[0] *  (n+1) for _ in range(m+1)]
        
        path[1][1] = 1 


        for i in range(1,m+1):
            for j in range(1,n+1):
                
                if i == 1 and j == 1 :
                    continue

                if obstacleGrid[i-1][j-1] == 1 :
                    continue 
            
                path[i][j] = path[i-1][j] + path[i][j-1]

        
        
        return path[m][n]