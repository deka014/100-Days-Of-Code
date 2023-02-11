# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Medium
# 5.7K
# 85
# Companies

# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:

# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

# Example 2:

# Input: inorder = [-1], postorder = [-1]
# Output: [-1]

 

# Constraints:

#     1 <= inorder.length <= 3000
#     postorder.length == inorder.length
#     -3000 <= inorder[i], postorder[i] <= 3000
#     inorder and postorder consist of unique values.
#     Each value of postorder also appears in inorder.
#     inorder is guaranteed to be the inorder traversal of the tree.
#     postorder is guaranteed to be the postorder traversal of the tree.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder, postorder) :
        inMap = {}

        for i in range(len(inorder)):
            inMap[inorder[i]] = i
        
        def build(instart,inend,postart):

            if postart < 0 or instart > inend :
                return None

            node = TreeNode(postorder[postart])

            inorderIndex = inMap[node.val]

            node.left = build(instart,inorderIndex-1,postart-1-(inend - inorderIndex))

            node.right = build(inorderIndex+1,inend,postart - 1)

            return node
        
        return build(0,len(inorder)-1,len(postorder)-1)
