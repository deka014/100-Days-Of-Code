# 1373. Maximum Sum BST in Binary Tree
# Hard
# 1.9K
# 153
# Companies

# Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

# Assume a BST is defined as follows:

#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

 

# Example 1:

# Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# Output: 20
# Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

# Example 2:

# Input: root = [4,3,null,1,2]
# Output: 2
# Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

# Example 3:

# Input: root = [-4,-2,-5]
# Output: 0
# Explanation: All values are negatives. Return an empty BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#note Global sum is used because sometimes the sum of the tree is not the max sum of the tree that is passed on 


class Solution:
    def maxSumBST(self, root) -> int:
        self.globalSum = 0
        def rec(root):

            if root is None :
                return 0 , float("-inf") , float("inf")
            
            SumLeft , leftHigh , leftLow = rec(root.left)
            SumRight , rightHigh , rightLow = rec(root.right)

            
            if root.val > leftHigh and root.val < rightLow:

                tempSum = SumLeft + SumRight + root.val
                self.globalSum = max(tempSum , self.globalSum)
                return tempSum, max(leftHigh,rightHigh,root.val) , min(leftLow,rightLow,root.val)

            return max(SumLeft,SumRight) , float("inf") , float("-inf")
        
        ans , high , low = rec(root)

        return self.globalSum








