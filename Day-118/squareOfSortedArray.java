// 977. Squares of a Sorted Array
// Solved
// Easy
// Topics
// Companies

// Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

// Example 1:

// Input: nums = [-4,-1,0,3,10]
// Output: [0,1,9,16,100]
// Explanation: After squaring, the array becomes [16,1,0,9,100].
// After sorting, it becomes [0,1,9,16,100].

// Example 2:

// Input: nums = [-7,-3,2,3,11]
// Output: [4,9,9,49,121]

 

// Constraints:

//     1 <= nums.length <= 104
//     -104 <= nums[i] <= 104
//     nums is sorted in non-decreasing order.

 
// Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?




class Solution {
    public int[] sortedSquares(int[] nums) {
        int positiveStart = nums.length-1;
        int ans[] = new int[nums.length];
        int index = 0;

        for (int i=0;i<nums.length;i++){
            if (nums[i]>=0){
                positiveStart = i;
                break;
            }
        }

        int goahead = positiveStart;
        int goback = goahead-1;
        
        while (goahead<nums.length && goback>=0){
            int negSquare = nums[goback] * nums[goback];
            int posSquare = nums[goahead] * nums[goahead];

            if (negSquare > posSquare){
                ans[index] = posSquare;
                goahead+=1;
            }else {
                ans[index] = negSquare;
                goback-=1;
            }
            index+=1;
        }

        while (goahead < nums.length){
            ans[index] = nums[goahead]*nums[goahead];
            goahead+=1;
            index+=1;
        }

        while (goback >= 0){
            ans[index] = nums[goback] * nums[goback];
            goback-=1;
            index+=1;
        }

        return ans;


    }
}