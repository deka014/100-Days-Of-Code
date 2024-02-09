# 368. Largest Divisible Subset
# Medium
# 5.6K
# 253
# Companies

# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

#     answer[i] % answer[j] == 0, or
#     answer[j] % answer[i] == 0

# If there are multiple solutions, return any of them.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,2]
# Explanation: [1,3] is also accepted.

# Example 2:

# Input: nums = [1,2,4,8]
# Output: [1,2,4,8]

 

# Constraints:

#     1 <= nums.length <= 1000
#     1 <= nums[i] <= 2 * 109
#     All the integers in nums are unique.







class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        #just check if the max is divisible or not
        maxi  = 1 
        lastindex = 0
        nums.sort()
        dp = [1 for _ in range(len(nums))]
        hashed = [i for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):

                if nums[i] % nums[j] == 0 and 1+dp[j]>dp[i]:
                    dp[i] = dp[j]+1
                    hashed[i] = j
            
            if dp[i] > maxi :
                maxi = dp[i]
                lastindex = i

        ans = [nums[lastindex]]

        while hashed[lastindex] != lastindex :
            lastindex = hashed[lastindex]
            ans.append(nums[lastindex])

        return ans
