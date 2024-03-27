// 713. Subarray Product Less Than K
// Solved
// Medium
// Topics
// Companies
// Hint

// Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

// Example 1:

// Input: nums = [10,5,2,6], k = 100
// Output: 8
// Explanation: The 8 subarrays that have product less than 100 are:
// [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
// Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

// Example 2:

// Input: nums = [1,2,3], k = 0
// Output: 0

 

// Constraints:

//     1 <= nums.length <= 3 * 104
//     1 <= nums[i] <= 1000
//     0 <= k <= 106

// Seen this question in a real interview before?
// 1/4

class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int l=0;
        int r = 0;
        int ans = 0;
        int currprod = 1;
        int n = nums.length;

        // while(r<n){
        //     if(l==r){
        //         if (nums[r]<k){
        //             ans+=1;
        //             currprod *= nums[r];
        //             r+=1;
        //         }
        //         else{
        //             currprod=1;
        //             r+=1;
        //             l+=1;
        //         }
        //     }
        //     else{
        //         currprod *= nums[r];
        //         if (currprod < k ){
        //             ans+=(1+r-l);
        //             r+=1;
        //         }
        //         else{
        //             while(!(currprod< k) && l<r){
        //                 currprod /= nums[l];
        //                 l+=1;
        //             }
        //             currprod /= nums[r];
        //         }
        //     }
        // }

        if (k<=1){
            return 0;
        }

        while(r<n){
            currprod *= nums[r];

            while (currprod>=k){
                currprod /= nums[l];
                l+=1;
            }

            ans+=(r-l+1);
            r+=1;

        }

        return ans;
    }
}


// 10 5 2 20          
// i
//      j

// 10 5 1 20
// l  
//    r


// 10 5 2 
//    i
//      j