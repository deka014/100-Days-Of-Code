# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Medium
# 12.1K
# 358
# Companies

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:

# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        
        inMap = {}

        for i in range(len(inorder)):
            inMap[inorder[i]] = i
        
        def build(instart,inend,prstart):

            if prstart >= len(preorder) or instart > inend :
                return None

            node = TreeNode(preorder[prstart])

            inorderIndex = inMap[node.val]

            node.left = build(instart,inorderIndex-1,prstart + 1)

            node.right = build(inorderIndex+1,inend,prstart+1+(inorderIndex - instart))

            return node
        
        return build(0,len(inorder)-1,0)


            




