# 101. Symmetric Tree
# Easy
# 12.2K
# 275
# Companies

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:

# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:

# Input: root = [1,2,2,null,3,null,3]
# Output: false


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):

        q = [root]
        
        while q :
            level = []
            for _ in range(len(q)):

                curr = q.pop(0)
                

                if curr is not None :
                    level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
                else :
                    level.append(None)
        
            if len(level) > 1 and len(level) % 2 != 0 :
                return False
            else :
                ptr1 = 0
                ptr2 = len(level)-1

                while ptr1 <= ptr2 :
                    if level[ptr1] != level[ptr2]:
                        return False
                    ptr1+=1
                    ptr2-=1
        
        return True

                


                    

