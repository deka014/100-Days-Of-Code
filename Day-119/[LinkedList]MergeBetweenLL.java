// Merge In Between Linked Lists
// Solved
// Medium
// Topics
// Companies
// Hint

// You are given two linked lists: list1 and list2 of sizes n and m respectively.

// Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

// The blue edges and nodes in the following figure indicate the result:

// Build the result list and return its head.

 

// Example 1:

// Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
// Output: [10,1,13,1000000,1000001,1000002,5]
// Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

// Example 2:

// Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
// Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
// Explanation: The blue edges and nodes in the above figure indicate the result.

 

// Constraints:

//     3 <= list1.length <= 104
//     1 <= a <= b < list1.length - 1
//     1 <= list2.length <= 104


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
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {

        ListNode l2end = list2 ;
        ListNode l1 = list1;
        ListNode l1bisect1 = null;
        ListNode l1bisect2 = null;
        int count = 0;

        while (l2end.next != null){
            l2end = l2end.next;
        }

        while(l1!=null){
            
            if (count+1==a){
                l1bisect1 = l1;
            }

            if(count==b+1){
                l1bisect2 = l1;
                break;
            }

            l1 = l1.next;
            count+=1;
        }

        l1bisect1.next = list2;
        l2end.next = l1bisect2;

        return list1;
    }
}

// Complexity Analysis

// The time complexity for this approach is O(n) where n is the number of nodes in list1.

