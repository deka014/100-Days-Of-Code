
# 100. Same Tree
# Easy
# 8.8K
# 180
# Companies

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:

# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:

# Input: p = [1,2,1], q = [1,1,2]
# Output: false

 

# Constraints:

#     The number of nodes in both trees is in the range [0, 100].
#     -104 <= Node.val <= 104

# Accepted
# 1.4M
# Submissions
# 2.5M


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) :
        
        l = [(p,q)]

        while l :
            curr1 , curr2 = l.pop()


            if curr1 is None and curr2 is None :
                continue

            if curr1 is None and curr2 is not None or curr1 is not None and curr2 is None :
                return False
            
            if curr1.val != curr2.val :
                return False


            l.append((curr1.right,curr2.right))

        
            l.append((curr1.left,curr2.left))
            
        
        return True

        


            


