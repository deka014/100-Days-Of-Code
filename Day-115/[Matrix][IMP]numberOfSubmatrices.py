# 1074. Number of Submatrices That Sum to Target
# Hard
# 3.5K
# 94
# Companies

# Given a matrix and a target, return the number of non-empty submatrices that sum to target.

# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 

# Example 1:

# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.

# Example 2:

# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

# Example 3:

# Input: matrix = [[904]], target = 0
# Output: 0

 

# Constraints:

#     1 <= matrix.length <= 100
#     1 <= matrix[0].length <= 100
#     -1000 <= matrix[i] <= 1000
#     -10^8 <= target <= 10^8

# Accepted
# 129.5K
# Submissions
# 176.5K
# Acceptance Rate
# 73.4%

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(1,cols):
                matrix[i][j] += matrix[i][j-1]

        ans = 0

        for startcol in range(0,cols):
            for j in range(startcol,cols):

                countmap = {0:1}

                currsum= 0

                for i in range(0,rows):
                    top = matrix[i][startcol-1] if startcol > 0 else 0
                    currsum+= matrix[i][j] - top

                    if currsum - target in countmap :
                        ans+= countmap[currsum-target]

                    if currsum in countmap :
                        countmap[currsum]+=1
                    else :
                        countmap[currsum] = 1 
        
        return ans

