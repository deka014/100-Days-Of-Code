#     LeetCode Logo

# Daily Question
# Premium
# 23
# 779. K-th Symbol in Grammar
# Medium
# 3.4K
# 351
# Companies

# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

#     For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.

# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

 

# Example 1:

# Input: n = 1, k = 1
# Output: 0
# Explanation: row 1: 0

# Example 2:

# Input: n = 2, k = 1
# Output: 0
# Explanation: 
# row 1: 0
# row 2: 01

# Example 3:

# Input: n = 2, k = 2
# Output: 1
# Explanation: 
# row 1: 0
# row 2: 01

 

# Constraints:

#     1 <= n <= 30
#     1 <= k <= 2n - 1

# Accepted
# 168.7K
# Submissions
# 372.7K
# Acceptance Rate
# 45.3%

import math
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

    #             0
    #         0       1
    #     0       1 1        0
    
    # 0      1 1   01  0   0       1

    # 2powern
    # ceil index//2 of the prev

    # 1 2 4 8

    # 0 1 0 1

    # 0-01
    # 1-10

        ans = 0 

        if n == 1 :
            return ans

        indexmap = {
            
            0 : [0,1],
            1 : [1,0]
        }

        trail = []

        while n >= 2 :
            trail.append(k)
            k = (k+1)//2
            n-=1
        
        for i in range(len(trail)-1,-1,-1):
            ans = indexmap[ans][(trail[i]+1)%2]

        return ans
