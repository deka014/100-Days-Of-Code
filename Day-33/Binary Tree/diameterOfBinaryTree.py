# 543. Diameter of Binary Tree
# Easy
# 10.7K
# 673
# Companies

# Given the root of a binary tree, return the length of the diameter of the tree.

# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

 

# Example 1:

# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

# Example 2:

# Input: root = [1,2]
# Output: 1

class Solution:
    def diameterOfBinaryTree(self, root) :

        def rec(node):

            if node is None :
                return (0,0)
            
            lh,lmaxDiam = rec(node.left) 
            rh,rmaxDiam = rec(node.right) 


            return (max(lh,rh) + 1, max(lh+rh+1 , lmaxDiam , rmaxDiam) )

        
        height , ans = rec(root)

        return ans - 1
