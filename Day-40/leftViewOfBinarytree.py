# Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.

# Left view of following tree is 1 2 4 8.

#           1
#        /     \
#      2        3
#    /     \    /    \
#   4     5   6    7
#    \
#      8   

# Example 1:

# Input:
#    1
#  /  \
# 3    2
# Output: 1 3


def LeftView(root):
    ans = []
    stack = [(root,0)] #root and level
    maxlevel = -1
    
    while stack :
        curr,level  = stack.pop()
        
        if curr is not None : 
            if level > maxlevel : 
                ans.append(curr.data)
                maxlevel = level
                
            stack.append((curr.right,level+1))
            stack.append((curr.left,level+1))
        
    return ans
