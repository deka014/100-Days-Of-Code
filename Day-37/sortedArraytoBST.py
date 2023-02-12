# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums) :
        

        def rec(l,r):

            if l > r :
                return None

            mid = (l + r) // 2 

            root = TreeNode(nums[mid])

            root.right = rec(mid+1,r)
            root.left = rec(l,mid-1)

            return root

        return rec(0,len(nums)-1)



