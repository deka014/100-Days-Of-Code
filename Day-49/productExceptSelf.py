# 238. Product of Array Except Self
# Medium
# 18.4K
# 1K
# Companies

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]


class Solution:
    def productExceptSelf(self, nums):
        # use post and pre technique

        output = [1]*len(nums)
        pre = 1
        post = 1
        for i in range(1,len(nums)):
            output[i] = nums[i-1] * pre
            pre = output[i]
        
        for j in range(len(nums)-2,-1,-1):
            output[j] = nums[j+1] * post * output[j]
            post = nums[j+1] * post


        return output