# Bottom View of Binary Tree
# MediumAccuracy: 54.18%Submissions: 152K+Points: 4
# Lamp
# Struggling with Cracking Interviews? Click here to end your problems!

# Given a binary tree, print the bottom view from left to right.
# A node is included in bottom view if it can be seen when we look at the tree from bottom.

#                       20
#                     /    \
#                   8       22
#                 /   \        \
#               5      3       25
#                     /   \      
#                   10    14

# For the above tree, the bottom view is 5 10 3 14 25.
# If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal. For example, in the below diagram, 3 and 4 are both the bottommost nodes at horizontal distance 0, we need to print 4.

#                       20
#                     /    \
#                   8       22
#                 /   \     /   \
#               5      3 4     25
#                      /    \      
#                  10       14

# For the above tree the output should be 5 10 4 14 25.

# Note: The Input/Output format and Example given are used for the system's internal purpose, and should be used by a user for Expected Output only. As it is a function problem, hence a user should not read any input from the stdin/console. The task is to complete the function specified, and not to write the full code.
 

# Example 1:

# Input:
#        1
#      /   \
#     3     2
# Output: 3 1 2
# Explanation:
# First case represents a tree with 3 nodes
# and 2 edges where root is 1, left child of
# # 1 is 3 and right child of 1 is 2



class Solution:
    def bottomView(self, root):
        # code here
        ans = []
        horizlinevalue = {}
        q = [(root , 0)]  #root and horizational distance value (hd)
        while q:
            curr,hd = q.pop(0)
            
            if curr is not None : 
                horizlinevalue[hd] = curr.data
                q.append((curr.left,hd-1))
                q.append((curr.right,hd+1))
        
        for i in sorted(horizlinevalue.keys()):
            ans.append(horizlinevalue[i])
        
        return ans