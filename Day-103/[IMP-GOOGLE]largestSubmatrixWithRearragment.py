# 1727. Largest Submatrix With Rearrangements
# Medium
# 1.4K
# 60
# Companies

# You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

# Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.

 

# Example 1:

# Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
# Output: 4
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 4.

# Example 2:

# Input: matrix = [[1,0,1,0,1]]
# Output: 3
# Explanation: You can rearrange the columns as shown above.
# The largest submatrix of 1s, in bold, has an area of 3.

# Example 3:

# Input: matrix = [[1,1,0],[1,0,1]]
# Output: 2
# Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.

 

# Constraints:

#     m == matrix.length
#     n == matrix[i].length
#     1 <= m * n <= 105
#     matrix[i][j] is either 0 or 1.

# Accepted
# 36.4K
# Submissions
# 51.1K
# Acceptance Rate
# 71.2%

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:


        # 1 x 
        # 1 1 1
        # 1 1 x

        prev = [] #height,col

        m = len(matrix)
        n = len(matrix[0])
        ans = 0

        for i in range(m):
            newrow = []
            visited = set()
            for h,c in prev:
                    if matrix[i][c] == 1 :
                        newrow.append((h+1,c))
                        visited.add(c)

            for j in range(n):
                if matrix[i][j] == 1 and not j in visited:
                    newrow.append((1,j))
            

            for k in range(len(newrow)):
                ans = max(ans,newrow[k][0] * (k+1))

            prev = newrow

                
        return ans
