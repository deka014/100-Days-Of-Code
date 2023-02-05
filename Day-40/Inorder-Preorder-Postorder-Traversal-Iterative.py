#the iterative way


class Solution:
    def inorderTraversal(self, root) :
        ans = []
        stack = []
        
        while root is not None or stack : 
            while root is not None : 
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            ans.append(root.val)
            root = root.right
        
        return ans


class Solution:
    def preorderTraversal(self, root):

        ans = []
        stack = [root]

        while stack : 
            curr = stack.pop()
            if curr is None : 
                continue
            ans.append(curr.val)    
            stack.append(curr.right)
            stack.append(curr.left)
            
        return ans


class Solution:
    def postorderTraversal(self, root):
        
        ans = []
        stack = [(root,False)]

        while stack :
            node , visited = stack.pop()
            if node is None :
                continue
            
            if visited : 
                ans.append(node.val)
            else :
                stack.append((node,True))
                stack.append((node.right,False))
                stack.append((node.left,False))

        return ans