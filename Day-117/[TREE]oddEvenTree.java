// 1609. Even Odd Tree
// Medium
// 1.7K
// 87
// Companies

// A binary tree is named Even-Odd if it meets the following conditions:

//     The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
//     For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
//     For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).

// Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

 

// Example 1:

// Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
// Output: true
// Explanation: The node values on each level are:
// Level 0: [1]
// Level 1: [10,4]
// Level 2: [3,7,9]
// Level 3: [12,8,6,2]
// Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.

// Example 2:

// Input: root = [5,4,2,3,3,7]
// Output: false
// Explanation: The node values on each level are:
// Level 0: [5]
// Level 1: [4,2]
// Level 2: [3,3,7]
// Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.

// Example 3:

// Input: root = [5,9,1,3,5,7]
// Output: false
// Explanation: Node values in the level 1 should be even integers.

 

// Constraints:

//     The number of nodes in the tree is in the range [1, 105].
//     1 <= Node.val <= 106

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.ArrayDeque;
import java.util.Queue;
import javafx.util.Pair;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Pair {
    private TreeNode key;
    private Integer value;

    public Pair(TreeNode key, Integer value){
        this.key = key;
        this.value = value;
    }

    public TreeNode getKey(){
        return key;
    }

    public Integer getValue(){
        return value;
    }

}

class Solution {
    public boolean isEvenOddTree(TreeNode root) {
        Queue<Pair<TreeNode,Integer>> q = new ArrayDeque<>(); //val,level
        q.offer(new Pair<>(root,0));
        int currlevel = 0;
        int lastval = -1;

        

        while (!q.isEmpty()){
            Pair<TreeNode,Integer> node = q.poll();
            TreeNode currNode = node.getKey();
            int level = node.getValue();

            if (level != currlevel){
                currlevel = level;
                lastval = currNode.val;

                if ((level%2==0) && (currNode.val%2==0)){
                    return false;
                }
                if ((level%2!=0) && (currNode.val%2!=0)){
                    return false;
                }
            }
            else {

            if(level%2 == 0){
                if ((currNode.val%2==0)||currNode.val<=lastval ){
                    System.out.println(currNode.val);
                    return false;
                }
            }
            else {
                if((currNode.val%2!=0) || currNode.val>=lastval){
                    System.out.println(currNode.val);
                    return false;
                }
            }
            }

            lastval = currNode.val;

            if (currNode.left != null){
                q.offer(new Pair<>(currNode.left,level+1));
            }

            if (currNode.right != null){
                q.offer(new Pair<>(currNode.right,level+1));
            }


        }

        return true;


        
    }
}

