# 1631. Path With Minimum Effort
# Medium
# 5.2K
# 175
# Companies

# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

# Example 1:

# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

# Example 2:

# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

# Example 3:

# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.

 

# Constraints:

#     rows == heights.length
#     columns == heights[i].length
#     1 <= rows, columns <= 100
#     1 <= heights[i][j] <= 106

# Accepted
# 199.7K
# Submissions
# 340K


# import heapq
# class Solution:
#     def minimumEffortPath(self, heights: List[List[int]]) -> int:

#         row = len(heights)
#         col = len(heights[0])

#         adaj =  {}

#         for i in range(row) :
#             for j in range(col) :
#                 adaj[(i,j)] = []

#         nrow = [-1,0,1,0]
#         ncol = [0,1,0,-1]

#         distance = [[10**6 + 1] * col for i in range(row)]

#         for i in range(row):
#             for j in range(col):

#                 for index in range(4) :

#                     r = nrow[index]
#                     c = ncol[index]

#                     if i+r < 0 or i+r >= row or j+c < 0 or j+c >= col:
#                         continue

#                     diff = abs(heights[i+r][j+c] - heights[i][j])
#                     adaj[(i,j)].append([(i+r,j+c),diff])

        
#         minh = [[0,0,0]] #cost , (row , col)

#         while minh :


#             ans = heapq.heappop(minh)
#             newdist, i,j = ans

#             if i == row -1 and j == col - 1 :
#                 return newdist

#             for neigh in adaj[(i,j)]:
                
#                 neighi = neigh[0][0]
#                 neighj = neigh[0][1]
                
#                 neighdist = max(neigh[1],newdist)

#                 if distance[neighi][neighj] > neighdist :
#                     distance[neighi][neighj] = neighdist
                
#                 heapq.heappush(minh,[neighdist,neighi,neighj])
        
#         return distance[row-1][col-1]
            

import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        adaj = {}

        for i in range(row):
            for j in range(col):
                adaj[(i, j)] = []

        nrow = [-1, 0, 1, 0]
        ncol = [0, 1, 0, -1]

        distance = [[float('inf')] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                for index in range(4):
                    r = nrow[index]
                    c = ncol[index]

                    if 0 <= i + r < row and 0 <= j + c < col:
                        diff = abs(heights[i + r][j + c] - heights[i][j])
                        adaj[(i, j)].append(((i + r, j + c), diff))

        minh = [(0, 0, 0)]  # cost , (row , col)

        while minh:
            newdist, i, j = heapq.heappop(minh)

            if i == row - 1 and j == col - 1:
                return newdist

            for neigh in adaj[(i, j)]:
                neighi, neighj = neigh[0]
                neighdist = max(neigh[1], newdist)

                if distance[neighi][neighj] > neighdist:
                    distance[neighi][neighj] = neighdist
                    heapq.heappush(minh, (neighdist, neighi, neighj))




        