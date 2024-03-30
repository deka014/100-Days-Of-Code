// 992. Subarrays with K Different Integers
// Solved
// Hard
// Topics
// Companies

// Given an integer array nums and an integer k, return the number of good subarrays of nums.

// A good array is an array where the number of different integers in that array is exactly k.

//     For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.

// A subarray is a contiguous part of an array.

 

// Example 1:

// Input: nums = [1,2,1,2,3], k = 2
// Output: 7
// Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

// Example 2:

// Input: nums = [1,2,1,3,4], k = 3
// Output: 3
// Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

 

// Constraints:

//     1 <= nums.length <= 2 * 104
//     1 <= nums[i], k <= nums.length

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        int atmostk = atmostMdistinctelements(nums,k);
        int atmostlessk = atmostMdistinctelements(nums,k-1);

        return atmostk - atmostlessk;
    }

    public int atmostMdistinctelements(int[] nums, int m){

        Map<Integer,Integer> mp = new HashMap<>();
        int l = 0;
        int r = 0;
        int ans = 0;
        int n = nums.length;

        while (r<n){
            mp.put(nums[r],mp.getOrDefault(nums[r],0)+1);

            while(mp.size() > m){
                if(mp.get(nums[l]) == 1){
                    mp.remove(nums[l]);
                }
                else {
                    mp.put(nums[l],mp.get(nums[l])-1);
                }
                l+=1;
            }

            ans+=(1+r-l);
            r+=1;
        }

        return ans;
    }
}