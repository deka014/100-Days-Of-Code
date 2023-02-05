# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        ans = []

        def recSol(root,ans):
            if root is None:
                return
            
            recSol(root.left,ans)
            ans.append(root.val)
            recSol(root.right,ans)
        
        recSol(root,ans)

        return ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root ) :
        ans = []

        self.helper(root,ans)
        return ans
    def helper(self,root,ans):
        if root is None :
            return 
        ans.append(root.val)
        self.helper(root.left,ans)
        self.helper(root.right,ans)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root) :
        
        ans = []
        self.helper(root,ans)
        return ans

    def helper(self,root,ans):
        if root is None :
            return 
        
        self.helper(root.left,ans)
        self.helper(root.right,ans)
        ans.append(root.val)
        

