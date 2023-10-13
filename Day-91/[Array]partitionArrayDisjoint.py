# 915. Partition Array into Disjoint Intervals
# Medium
# 1.6K
# 74
# Companies

# Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:

#     Every element in left is less than or equal to every element in right.
#     left and right are non-empty.
#     left has the smallest possible size.

# Return the length of left after such a partitioning.

# Test cases are generated such that partitioning exists.

 

# Example 1:

# Input: nums = [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]

# Example 2:

# Input: nums = [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]

 

# Constraints:

#     2 <= nums.length <= 105
#     0 <= nums[i] <= 106
#     There is at least one valid answer for the given input.

# Accepted
# 78.6K
# Submissions
# 161.5K
# Acceptance Rate
# 48.7%

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:

        ans = 0
        prevmax = nums[0]
        maxleft = nums[0]

        for i in range(1,len(nums)):
            prevmax = max(prevmax,nums[i])
            if nums[i] < maxleft :
                maxleft = prevmax
                ans = i
        return ans+1

    
        # 5 0 10 4 7 9 6 12   ans - 5 0 10 4 7 9 6 12


        # no partition conditon 

        # if there is a number in left greater than rights max 
        # and there is a number in right smaller than rights max




            





