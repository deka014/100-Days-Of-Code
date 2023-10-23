# 342. Power of Four
# Easy
# 3.6K
# 365
# Companies

# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4x.

 

# Example 1:

# Input: n = 16
# Output: true

# Example 2:

# Input: n = 5
# Output: false

# Example 3:

# Input: n = 1
# Output: true

 

# Constraints:

#     -231 <= n <= 231 - 1

 
# Follow up: Could you solve it without loops/recursion?
# Accepted
# 572.1K
# Submissions
# 1.2M
# Acceptance Rate
# 47.4%

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n == 1 :
            return True
        if n <= 0 or n % 4 != 0 :
            return False 

        return self.isPowerOfFour(n//4)