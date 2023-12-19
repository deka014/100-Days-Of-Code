# 661. Image Smoother
# Easy
# 869
# 2.6K
# Companies

# An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).

# Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.

 

# Example 1:

# Input: img = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[0,0,0],[0,0,0],[0,0,0]]
# Explanation:
# For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0

# Example 2:

# Input: img = [[100,200,100],[200,50,200],[100,200,100]]
# Output: [[137,141,137],[141,138,141],[137,141,137]]
# Explanation:
# For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
# For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
# For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138

 

# Constraints:

#     m == img.length
#     n == img[i].length
#     1 <= m, n <= 200
#     0 <= img[i][j] <= 255

# Accepted
# 123K
# Submissions
# 192.5K
# Acceptance Rate
# 63.9%

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        # 1,1   -> 00,01,02,10,11,12,20,21,22

        def mask(oldi,oldj):
            count = 0
            total = 0
            for i in range(oldi-1,oldi+2):
                for j in range(oldj-1,oldj+2):
                    
                    if i>-1 and i <len(img) and j>-1 and j<len(img[0]):
                        
                        count+=1
                        total += img[i][j]


            return total//count

        
        ans = [[0]*len(img[0]) for _ in range(len(img))]

        for i in range(len(img)):
            for j in range(len(img[0])):
                
                ans[i][j] = mask(i,j)
        
        return ans