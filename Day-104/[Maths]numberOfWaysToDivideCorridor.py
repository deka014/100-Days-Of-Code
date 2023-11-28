# 2147. Number of Ways to Divide a Long Corridor
# Hard
# 618
# 67
# Companies

# Along a long library corridor, there is a line of seats and decorative plants. You are given a 0-indexed string corridor of length n consisting of letters 'S' and 'P' where each 'S' represents a seat and each 'P' represents a plant.

# One room divider has already been installed to the left of index 0, and another to the right of index n - 1. Additional room dividers can be installed. For each position between indices i - 1 and i (1 <= i <= n - 1), at most one divider can be installed.

# Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants. There may be multiple ways to perform the division. Two ways are different if there is a position with a room divider installed in the first way but not in the second way.

# Return the number of ways to divide the corridor. Since the answer may be very large, return it modulo 109 + 7. If there is no way, return 0.

 

# Example 1:

# Input: corridor = "SSPPSPS"
# Output: 3
# Explanation: There are 3 different ways to divide the corridor.
# The black bars in the above image indicate the two room dividers already installed.
# Note that in each of the ways, each section has exactly two seats.

# Example 2:

# Input: corridor = "PPSPSP"
# Output: 1
# Explanation: There is only 1 way to divide the corridor, by not installing any additional dividers.
# Installing any would create some section that does not have exactly two seats.

# Example 3:

# Input: corridor = "S"
# Output: 0
# Explanation: There is no way to divide the corridor because there will always be a section that does not have exactly two seats.

 

# Constraints:

#     n == corridor.length
#     1 <= n <= 105
#     corridor[i] is either 'S' or 'P'.

# Accepted
# 30K
# Submissions
# 62.8K
# Acceptance Rate
# 47.8%

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        # SSPPSPS

        # 110010111

        # 11-00-101-0-11

        # 3 - 1 - 2

        # 2*3 = 6

        totalS = 0

        for letter in corridor :
            if letter == "S" :
                totalS+=1
        
        if  totalS == 0 or totalS % 2 != 0 :
            return 0

        count = 0
        ans = 1
        permutations = 1
        for letter in corridor:
            
            if letter == "S":
                if count == 2:
                    ans*=permutations
                    permutations=1
                    count=1
                else :
                    count+=1
            else :
                if count == 2:
                    permutations+=1
    
        return ans% (10**9 + 7)