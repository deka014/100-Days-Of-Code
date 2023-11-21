# 1814. Count Nice Pairs in an Array
# Medium
# 1.2K
# 50
# Companies

# You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

#     0 <= i < j < nums.length
#     nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])

# Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: nums = [42,11,1,97]
# Output: 2
# Explanation: The two pairs are:
#  - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
#  - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.

# Example 2:

# Input: nums = [13,10,35,24,76]
# Output: 4

 

# Constraints:

#     1 <= nums.length <= 105
#     0 <= nums[i] <= 109

# Accepted
# 50.1K
# Submissions
# 107.7K
# Acceptance Rate
# 46.5%

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        # 42 11 1 97 
        
        # 24 11 1 79 

        # x0 + y1 = x1 + y0

        # x0 - x1 = y0 - y1

        def rev(n):
        
            ans = 0
            while n != 0:
                rem = n%10
                ans = ans*10 + rem
                n = n//10
            
            return ans

        countnum = {}
        result = 0

        for num in nums :
            newnum = num - rev(num)

            if newnum in countnum :
                result += countnum[newnum]
                countnum[newnum]+=1
            else :
                countnum[newnum] = 1

        return result % (10**9 +7)