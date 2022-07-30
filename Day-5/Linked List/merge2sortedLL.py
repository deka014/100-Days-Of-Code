# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:

# Input: list1 = [], list2 = []
# Output: []

# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]


# https://leetcode.com/problems/merge-two-sorted-lists/


Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        i = list1
        j = list2
        result = ListNode()
        currentNode = result
        
        while i and j :
            if i.val < j.val:
                # temp1 = i.next
                currentNode.next = i
                currentNode = currentNode.next
                i = i.next
            else :
                # temp2 = j.next
                currentNode.next = j
                currentNode = currentNode.next
                j = j.next
            
        if i :
            currentNode.next = i
        if j :
            currentNode.next = j 
        
        return result.next
                
        