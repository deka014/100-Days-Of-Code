# 725. Split Linked List in Parts
# Medium
# 3.5K
# 284
# Companies

# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

# Return an array of the k parts.

 

# Example 1:

# Input: head = [1,2,3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but its string representation as a ListNode is [].

# Example 2:

# Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
# Output: [[1,2,3,4],[5,6,7],[8,9,10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

 

# Constraints:

#     The number of nodes in the list is in the range [0, 1000].
#     0 <= Node.val <= 1000
#     1 <= k <= 50

# Accepted
# 167.8K
# Submissions
# 267.4K
# Acceptance Rate
# 62.7%
# Seen this question in a real interview before?
# 1/4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        n = 0
        output = []

        front = head

        while front :
            n+=1
            front = front.next
        
        count = n // k
        rem  = n % k

        front = head
        toappend = head
        p1 = 0 
        p2 = 0

        

        while front :
            p1+=1
            extra = 1 if rem > 0 else 0

            if p1-p2 == count + extra:
                temp = front.next
                front.next = None
                output.append(toappend)
                toappend = temp
                front = temp
                p2 = p1
                rem-=1
                continue
            
            front = front.next
        
        
        if len(output) < k :
            for i in range(k-len(output)):
                output.append(None)

        return output





        