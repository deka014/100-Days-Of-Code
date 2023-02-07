# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:

# Input: root = [1]
# Output: [[1]]

# Example 3:

# Input: root = []
# Output: []


class Solution:
    def levelOrder(self, root) :

        

        if root == None :
            return []

        ans = []

        q = [root]

        while q : 
            temp = []
            for _ in range(len(q)):
                curr = q.pop(0)
                temp.append(curr.val)

                if curr.left is not None : 
                    q.append(curr.left)
                if curr.right is not None : 
                    q.append(curr.right)
            
            if temp :
                ans.append(temp)
                
        return ans