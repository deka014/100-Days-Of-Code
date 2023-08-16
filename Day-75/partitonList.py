# 86. Partition List
# Medium
# 6.8K
# 741
# Companies

# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

 

# Example 1:

# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]

 

# Constraints:

#     The number of nodes in the list is in the range [0, 200].
#     -100 <= Node.val <= 100
#     -200 <= x <= 200

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftending = None 
        leftstarting = None
        rightstarting = None 
        rightending = None 

        curr = head


        while curr!= None :

            if curr.val < x :
                if leftstarting == None :
                    leftstarting = curr

                if leftending != None :
                    leftending.next = curr

                leftending = curr
            
            else :
                if rightstarting == None : 
                    rightstarting = curr
                
                if rightending != None :
                    rightending.next = curr

                rightending = curr
            
            curr = curr.next
        
        if rightstarting == None or leftstarting == None :
            return head
        
        leftending.next = rightstarting
        rightending.next = None
    
        return leftstarting