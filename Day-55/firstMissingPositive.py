# 41. First Missing Positive
# Hard
# 14.4K
# 1.6K
# Companies

# Given an unsorted integer array nums, return the smallest missing positive integer.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.


# class Solution:
#   def firstMissingPositive(self, nums):
#     n = len(nums)
    
#     for i in range(n):
#         while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
#             nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
#     for i in range(n):
#         if nums[i] != i + 1:
#             return i + 1
    
#     return n + 1


class Solution:
    def firstMissingPositive(self, nums) :
        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            if 1 <= abs(nums[i]) <= len(nums) :

                if nums[abs(nums[i]) - 1 ] > 0 :
                    nums[abs(nums[i]) - 1] *= -1

                elif nums[abs(nums[i]) - 1] == 0 :
                    nums[abs(nums[i]) - 1 ] = -(len(nums) + 1)
 
        
        for i in range(len(nums)):
            if nums[i] >= 0 :
                return i+1
        
        return len(nums) + 1

        