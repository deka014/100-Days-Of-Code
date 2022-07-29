# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Input: nums = [5,4,-1,7,8]
# Output: 23

# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = nums[0]
        tempSum = 0
        i = 0 
        while i < len(nums) : 
            
            tempSum += nums[i]
            maxSum = max(tempSum, maxSum)
            
            if tempSum < 0 :
                i = i + 1
                tempSum = 0
            
            else :
                i+= 1
        
            
        return maxSum

# Intuiton: 
#         1) If the sum is negative, then we need to start from the next element.
#         2) If the sum is positive, then we need to keep adding the elements.
#         3) If the sum is 0, then we need to start from the next element.
#         Time Complexity: O(n)
#         Space Complexity: O(1)
