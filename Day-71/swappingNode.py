# 1721. Swapping Nodes in a Linked List
# Medium
# 4.9K
# 162
# Companies

# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]

# Example 2:

# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]

 

# Constraints:

#     The number of nodes in the list is n.
#     1 <= k <= n <= 105
#     0 <= Node.val <= 100

# Accepted
# 286.5K
# Submissions
# 417.7K
# Acceptance Rate
# 68.6%
# Seen this question in a real interview before?
# 1/4
# Yes
# No


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = None
        right = None
        temp = head
        dist = 1

        while temp.next != None:
            dist+= 1 
            temp = temp.next
            
        if dist == 1 :
            return head

        temp = head
        target = dist - k 
        i = 0

        while temp != None:
            if i == target : 
                right = temp
            if i == k-1 :
                left = temp
            
            temp = temp.next
            i+=1

        left.val , right.val = right.val , left.val 

        return head
        


        return head

        
