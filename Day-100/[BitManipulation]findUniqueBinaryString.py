# 1980. Find Unique Binary String
# Medium
# 1.4K
# 53
# Companies

# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

# Example 1:

# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.

# Example 2:

# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.

# Example 3:

# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

 

# Constraints:

#     n == nums.length
#     1 <= n <= 16
#     nums[i].length == n
#     nums[i] is either '0' or '1'.
#     All the strings of nums are unique.

# Accepted
# 75.6K
# Submissions
# 105.5K
# Acceptance Rate
# 71.6%


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        setnums = set(nums)
        
        
        shift = 0
        form = "0" + str(n) + "b"
        


        while shift < n :
            ans = str(format(1<<shift,form))
            if not ans in setnums :
                return ans
            shift+=1

        return str(format(0,form))
        


