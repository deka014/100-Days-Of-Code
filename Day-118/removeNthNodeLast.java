// 19. Remove Nth Node From End of List
// Medium
// 18.2K
// 765
// Companies

// Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

// Example 1:

// Input: head = [1,2,3,4,5], n = 2
// Output: [1,2,3,5]

// Example 2:

// Input: head = [1], n = 1
// Output: []

// Example 3:

// Input: head = [1,2], n = 1
// Output: [1]

 

// Constraints:

//     The number of nodes in the list is sz.
//     1 <= sz <= 30
//     0 <= Node.val <= 100
//     1 <= n <= sz

 

// Follow up: Could you do this in one pass?

 class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
    //     int k = 0;
    //     ListNode curr = head;
    //     while (curr!=null){
    //         k+=1;
    //         curr = curr.next;
    //     }
    //     curr = head;

    //     if (k-n == 0){
    //         return head.next;
    //     }
    //     for (int i = 1 ; i<= k-n ; i++){
    //         if (i== k-n){
    //             ListNode temp = curr.next;
    //             if (temp!=null){
    //                 curr.next = temp.next;
    //                 break;
    //             }
    //         }
    //         curr = curr.next;
    //     }
    //     return head;

    ListNode fast = head;
    ListNode slow = head;

    
    for (int i = 0 ; i < n ; i++){
        fast = fast.next;
        if (fast == null){
            return head.next;
        }
    }

    while (fast.next != null){
        fast = fast.next;
        slow = slow.next;
    }
    
    slow.next = slow.next.next;
    
    return head;
    }
}


