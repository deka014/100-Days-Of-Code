# Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
# Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

# Example 1:

# Input:
# N = 4
# m[][] = {{1, 0, 0, 0},
#          {1, 1, 0, 1}, 
#          {1, 1, 0, 0},
#          {0, 1, 1, 1}}
# Output:
# DDRDRR DRDDRR
# Explanation:
# The rat can reach the destination at 
# (3, 3) from (0, 0) by two paths - DRDDRR 
# and DDRDRR, when printed in sorted order 
# we get DDRDRR DRDDRR.

# Example 2:

# Input:
# N = 2
# m[][] = {{1, 0},
#          {1, 0}}
# Output:
# -1
# Explanation:
# No path exists and destination cell is 
# blocked.


#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # D L R U
        visited = [[0 for i in range(n)] for j in range(n)]
        output = []
        path = "DLRU"
        loopRow = [1,0,0,-1]
        loopCol = [0,-1,1,0]
        def solve(row,col,ans):
            
            if row == n-1 and col == n-1:
                output.append(ans.copy())
                return
            
            for i in range(4):
                nextR = row + loopRow[i]
                nextC = col + loopCol[i]
                if nextR >= 0 and nextR < n and nextC>=0 and nextC<n and visited[nextR][nextC] != 1 and m[nextR][nextC] == 1 :
                    visited[i][j] = 1
                    solve(nextR,nextC,ans+path[i])
                    visited[i][j] = 0
        
        solve(0,0,"")
        return output