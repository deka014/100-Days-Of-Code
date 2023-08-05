# 95. Unique Binary Search Trees II
# Medium
# 6.9K
# 447
# Companies

# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

# Example 1:

# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

# Example 2:

# Input: n = 1
# Output: [[1]]

 

# Constraints:

#     1 <= n <= 8


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        
        def rec(left,right):

            if left == right :
                return [TreeNode(left)]

            if left > right :
                return [None]
            
            res = []
            for val in range(left,right+1):
                for leftnode in rec(left,val-1):
                    for rightnode in rec(val+1,right):
                        
                        root = TreeNode(val,leftnode,rightnode)
                        res.append(root)

            return res

        return rec(1,n)
