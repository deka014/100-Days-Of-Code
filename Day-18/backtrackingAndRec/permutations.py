# 46. Permutations
# Medium

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:

# Input: nums = [1]
# Output: [[1]]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        
        def solve(nums,index):
            
            if index >= len(nums):
                
                output.append(nums.copy())
            
            for j in range(index,len(nums)):
                
                nums[j] , nums[index] = nums[index] , nums[j]
                
                solve(nums,index+1)
                
                nums[j] , nums[index] = nums[index] , nums[j]
                
        solve(nums,0)    
        return output
                
# Intuiton : Striver