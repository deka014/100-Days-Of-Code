# 1424. Diagonal Traverse II
# Medium
# 1.8K
# 131
# Companies

# Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

 

# Example 1:

# Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,4,2,7,5,3,8,6,9]

# Example 2:

# Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

 

# Constraints:

#     1 <= nums.length <= 105
#     1 <= nums[i].length <= 105
#     1 <= sum(nums[i].length) <= 105
#     1 <= nums[i][j] <= 105

# Accepted
# 95.3K
# Submissions
# 172.5K
# Acceptance Rate
# 55.3%
# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Discussion (45)
# Related Topics

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        sortarr = []

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                sortarr.append((i+j,i,nums[i][j]))

        sortarr.sort(key = lambda x : (x[0],-x[1]))
        
        output = []
        for summed,row, val in sortarr:
            output.append(val)

        return output

    