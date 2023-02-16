# 173. Binary Search Tree Iterator
# Medium
# 7.3K
# 439
# Companies

# Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

#     BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
#     boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
#     int next() Moves the pointer to the right, then returns the number at the pointer.

# Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

# You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

 

# Example 1:

# Input
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output
# [null, 3, 7, true, 9, true, 15, true, 20, false]

# Explanation
# BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
# bSTIterator.next();    // return 3
# bSTIterator.next();    // return 7
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 9
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 15
# bSTIterator.hasNext(); // return True
# bSTIterator.next();    // return 20
# bSTIterator.hasNext(); // return False


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        temp = root
        while temp is not None :
            self.stack.append(temp)
            temp = temp.left
            
        

    def next(self) -> int:
        curr = self.stack.pop()
        temp = curr.right
        while temp is not None :
            self.stack.append(temp)
            temp = temp.left
        return curr.val
            
        
        
    def hasNext(self) -> bool:
        if self.stack :
            return True 
        
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()