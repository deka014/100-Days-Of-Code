// 404. Sum of Left Leaves
// Solved
// Easy
// Topics
// Companies

// Given the root of a binary tree, return the sum of all left leaves.

// A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 

// Example 1:

// Input: root = [3,9,20,null,null,15,7]
// Output: 24
// Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

// Example 2:

// Input: root = [1]
// Output: 0

 

// Constraints:

//     The number of nodes in the tree is in the range [1, 1000].
//     -1000 <= Node.val <= 1000

// Seen this question in a real interview before?
// 1/5
// Yes
// No
// Accepted
// 553.8K
// Submissions
// 935.3K
// Acceptance Rate
// 59.2%


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        return recSol(root,false);
    }

    public int recSol(TreeNode node, boolean isLeft){
        if(node.left == null && node.right == null){
            if (isLeft){
                return node.val;
            }else{
                return 0;
            }
        }

        int ans = 0;
        if (node.left != null){
            ans+= recSol(node.left,true);
        }
        
        if (node.right != null){
            ans+= recSol(node.right,false);
        }

        return ans;
    }
}