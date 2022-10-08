# 16. 3Sum Closest
# Medium

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

 

# Constraints:

#     3 <= nums.length <= 1000
#     -1000 <= nums[i] <= 1000
#     -104 <= target <= 104


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        nums.sort()
        
        for i in range(len(nums) - 2):
            ptr1 = i+1
            ptr2 = len(nums) - 1
            
            
            while ptr1 < ptr2 :
                currentSum = nums[i] + nums[ptr1] + nums[ptr2]
                if abs(target - currentSum) < abs(target - result ):
                    result = currentSum

                if currentSum < target :
                    ptr1+=1
                else:
                    ptr2-=1
                # else :
                #     return target
                
                

            
        return result
            
            

