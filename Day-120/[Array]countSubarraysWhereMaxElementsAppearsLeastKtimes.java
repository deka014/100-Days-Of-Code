// 962. Count Subarrays Where Max Element Appears at Least K Times
// Solved
// Medium
// Topics
// Companies

// You are given an integer array nums and a positive integer k.

// Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

// A subarray is a contiguous sequence of elements within an array.

 

// Example 1:

// Input: nums = [1,3,2,3,3], k = 2
// Output: 6
// Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

// Example 2:

// Input: nums = [1,4,2,1], k = 3
// Output: 0
// Explanation: No subarray contains the element 4 at least 3 times.

 

// Constraints:

//     1 <= nums.length <= 105
//     1 <= nums[i] <= 106
//     1 <= k <= 105

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long countSubarrays(int[] nums, int k) {
       int maxnum = 0;
       int n = nums.length;
       long ans = 0;
       Map<Integer,Integer> mp = new HashMap<>();
       for (int num : nums){
        maxnum = Math.max(num,maxnum);
       }

        int l = 0;
        int r = 0;


        while(r<n){
            mp.put(nums[r],mp.getOrDefault(nums[r],0)+1);

            while(mp.getOrDefault(maxnum,0) >= k){
                ans+=(1+(n-r-1));
                mp.put(nums[l],mp.get(nums[l])-1);
                l+=1;
            }

            r+=1;

        }

        return ans;
    }
}

//max array appears atleast k times