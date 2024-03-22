// 234. Palindrome Linked List
// Solved
// Easy
// Topics
// Companies

// Given the head of a singly linked list, return true if it is a
// palindrome
// or false otherwise.

 

// Example 1:

// Input: head = [1,2,2,1]
// Output: true

// Example 2:

// Input: head = [1,2]
// Output: false

 

// Constraints:

//     The number of nodes in the list is in the range [1, 105].
//     0 <= Node.val <= 9

 
// Follow up: Could you do it in O(n) time and O(1) space?

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        //middle of the list and reversing

        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null;
        
        while(fast!=null && fast.next!=null){
            fast = fast.next.next;
            ListNode temp = slow.next;
            slow.next = prev;
            prev = slow;
            slow = temp;
        }

        //adjustments for even and odd palindrome
        //if the palindrome is odd then fast will not be null so increase slow by one

        if(fast!=null){
            slow=slow.next;
        }
        
        while(slow!=null){
            if (slow.val!=prev.val) {
                return false;
            }
            slow = slow.next;
            prev = prev.next;
        }

        return true;
    }
}


// 1 2 4 4 2 1
//       s 
//             f

// 1 2 4 2 1 
