# 515. Find Largest Value in Each Tree Row
# Medium
# 3.3K
# 105
# Companies

# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

# Example 1:

# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]

# Example 2:

# Input: root = [1,2,3]
# Output: [1,3]

 

# Constraints:

#     The number of nodes in the tree will be in the range [0, 104].
#     -231 <= Node.val <= 231 - 1

# Accepted
# 285.8K
# Submissions
# 438.1K
# Acceptance Rate
# 65.2%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if root == None :
            return []
        
        q = deque()
        q.append((root,0))

        ans = []
        temp = -2**31 - 1
        currlv = 0

        while q :

            node , lv = q.popleft()

            if node == None :
                continue
                
            if lv != currlv :
                currlv+=1
                ans.append(temp)
                temp = -2**31 -1
            
            temp = max(temp,node.val)
        
            q.append((node.left,currlv+1))
            q.append((node.right,currlv+1))

        ans.append(temp)

        return ans