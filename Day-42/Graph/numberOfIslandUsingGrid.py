# 200. Number of Islands
# Medium
# 19K
# 422
# Companies

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

 

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 300
#     grid[i][j] is '0' or '1'.


class Solution:
    def numIslands(self, grid):
        ans = 0


        def findIsland(n,m,grid):
            if n >= len(grid) or m >= len(grid[0]) or n < 0 or m < 0 :
                return 
            if grid[n][m] != "1" :
                return 
            grid[n][m] = "0"

            findIsland(n,m+1,grid)
            findIsland(n+1,m,grid)
            findIsland(n-1,m,grid)
            findIsland(n,m-1,grid)
        


        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] != "1" :
                    continue
                
                findIsland(i,j,grid)
                ans+=1
        
        return ans
                


