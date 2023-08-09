# 2616. Minimize the Maximum Difference of Pairs
# Medium
# 1.3K
# 125
# Companies

# You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

# Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

# Return the minimum maximum difference among all p pairs. We define the maximum of an empty set to be zero.

 

# Example 1:

# Input: nums = [10,1,2,7,1,3], p = 2
# Output: 1
# Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
# The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.

# Example 2:

# Input: nums = [4,2,1,2], p = 1
# Output: 0
# Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.

 

# Constraints:

#     1 <= nums.length <= 105
#     0 <= nums[i] <= 109
#     0 <= p <= (nums.length)/2

# Accepted
# 31.5K
# Submissions
# 77.5K
# Acceptance Rate
# 40.7%

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        if len(nums) == 0 or len(nums) == 1 or p == 0:
            return 0

        nums.sort()
        
        ans = []

        i = 1

        while i < len(nums):
            ans.append(nums[i] - nums[i-1])
            i+=1



        def isvalid(guess):
            j = 0
            temp = 0
            while j < len(ans):
                if ans[j] <= guess :
                    temp+=1
                    j+=2
                else :
                    j+=1
            
            if temp >= p:
                return True
            else :
                False 

        
        l , r = 0 , 10**9
        res = 10**9

        while l <= r :            

            m = l + (r-l) // 2 

            if isvalid(m):
                res = m 
                r = m - 1
            else :
                l = m + 1
        
        return res

            
                
    
            
            
        