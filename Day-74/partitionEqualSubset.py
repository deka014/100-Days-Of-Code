# 416. Partition Equal Subset Sum
# Medium
# 11.2K
# 203
# Companies

# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

 

# Constraints:

#     1 <= nums.length <= 200
#     1 <= nums[i] <= 100

# Accepted
# 676.3K
# Submissions
# 1.5M
# Acceptance Rate
# 46.2%
# Seen this question in a real interview before?
# 1/4
# Yes
# No

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        target = sum(nums) / 2 
        
        if target % 1 != 0 :
            return False 
        
        hashset  = {}
        
        print(target)
        
        def rec(s1,s2,i):
            
            if (s1,s2) in hashset :
                print("i ran" , s1,s2)
                return hashset[(s1,s2)]
            
            if s1 > target or s2 > target :
                return False
            
            if i == len(nums) and s1==s2:
                return True

            if i >= len(nums):
                return False
            
            hashset[(s1,s2)] = rec(s1+nums[i],s2,i+1) or rec(s1,s2 + nums[i],i+1)

            return hashset[(s1,s2)]

        
        return rec(0,0,0)