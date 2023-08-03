# You are given an m x n grid where each cell can have one of three values:

#     0 representing an empty cell,
#     1 representing a fresh orange, or
#     2 representing a rotten orange.

# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

 

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 10
#     grid[i][j] is 0, 1, or 2.

# Accepted
# 650.2K
# Submissions
# 1.2M

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]
        time = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    visited[i][j] = True

        # Helper function to check if a cell is within the grid boundaries
        def is_valid(x, y):
            return 0 <= x < row and 0 <= y < col

        # Perform BFS to rot the fresh oranges
        while q:
            x, y, time = q.pop(0)

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if is_valid(new_x, new_y) and not visited[new_x][new_y] and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 2
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y, time + 1))

        # Check if there are any fresh oranges left
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1

        return time