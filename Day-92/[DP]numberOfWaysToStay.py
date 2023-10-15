# 1269. Number of Ways to Stay in the Same Place After Some Steps
# Hard
# 1.1K
# 51
# Companies

# You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).

# Given two integers steps and arrLen, return the number of ways such that your pointer is still at index 0 after exactly steps steps. Since the answer may be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: steps = 3, arrLen = 2
# Output: 4
# Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
# Right, Left, Stay
# Stay, Right, Left
# Right, Stay, Left
# Stay, Stay, Stay

# Example 2:

# Input: steps = 2, arrLen = 4
# Output: 2
# Explanation: There are 2 differents ways to stay at index 0 after 2 steps
# Right, Left
# Stay, Stay

# Example 3:

# Input: steps = 4, arrLen = 2
# Output: 8

 

# Constraints:

#     1 <= steps <= 500
#     1 <= arrLen <= 106

# Accepted
# 54.4K
# Submissions
# 114.8K
# Acceptance Rate
# 47.4%


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        dp = {}

        def rec(remain,index):

            if index == arrLen or index == -1 :
                return 0
            
            if remain == 0 :
                return 1 if remain == index else 0

            if (remain , index) in dp :
                return dp[(remain,index)]
            

            # left 

            l = rec(remain-1,index+1)

            # right 

            r = rec(remain-1 , index-1)

            # stay

            s = rec(remain-1 , index)

            dp[(remain,index)] =  l + s + r

            return dp[(remain,index)]


        return rec(steps,0) % (10**9 + 7)
            
