# 103. Binary Tree Zigzag Level Order Traversal
# Medium
# 8.1K
# 212
# Companies

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

# Example 2:

# Input: root = [1]
# Output: [[1]]

# Example 3:

# Input: root = []
# Output: []

 

# Constraints:

#     The number of nodes in the tree is in the range [0, 2000].
#     -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root) :
        if root is None :
            return []

        ans = []
        level = 0
        q = [root]

        while q :
            
            temp = []
            for _ in range(len(q)):
                curr = q.pop(0)

                if curr is not None :
                    temp.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)

            if temp :
                if level % 2 == 0 :
                    ans.append(temp)
                else :
                    temp.reverse()
                    ans.append(temp)

            level+=1

        return ans




            
        



