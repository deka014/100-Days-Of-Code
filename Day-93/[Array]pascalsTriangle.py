# 119. Pascal's Triangle II
# Easy
# 4.5K
# 316
# Companies

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:

# Input: rowIndex = 0
# Output: [1]

# Example 3:

# Input: rowIndex = 1
# Output: [1,1]

 

# Constraints:

#     0 <= rowIndex <= 33

 

# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
# Accepted
# 787.6K
# Submissions
# 1.3M
# Acceptance Rate
# 62.9%

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        ans = [1,1]

        if rowIndex == 0 :
            return [1]

        if rowIndex == 1 :
            return ans

        for _ in range(2,rowIndex+1):
            prev = 1
            for i in range(1,len(ans)):
                
                temp = ans[i] + prev
                prev = ans[i]
                ans[i] = temp
            
            ans.append(1)

        return ans
