# 377. Combination Sum IV
# Medium
# 6.9K
# 622
# Companies

# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

# The test cases are generated so that the answer can fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.

# Example 2:

# Input: nums = [9], target = 3
# Output: 0

 

# Constraints:

#     1 <= nums.length <= 200
#     1 <= nums[i] <= 1000
#     All the elements of nums are unique.
#     1 <= target <= 1000

 

# Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        

        dp = {}
        nums.sort()
        def rec(total) : 
            
            
            if total == target:
                return 1

            if total in dp :
                return dp[total]
            
            temp = 0

            for num in nums : 
                
                if total + num > target :
                    break
                temp += rec(total+num)
            
            
            dp[total] = temp
            return temp

        rec(0)
        print(dp)
        return dp[0]



        