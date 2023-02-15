# you-are-given-a-bst-binary-search-tree-with-n-number-of-nodes-and-a-value-x-your-task-is-to-find-
# the-greatest-value-node-of-the-bst-which-is-smaller-than-or-equal-to-x


from os import *
from sys import *
from collections import *
from math import *




def floorInBST(root, X):
    ans = None
    # Write your Code here.
    curr = root
    while curr is not None :

        if curr.data == X :
            return curr.data
        
        if curr.data < X :
            ans = curr.data
            curr = curr.right
        
        else :
            curr = curr.left
    
    return ans


            
