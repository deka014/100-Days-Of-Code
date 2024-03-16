// 930. Binary Subarrays With Sum
// Solved
// Medium
// Topics
// Companies

// Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

// A subarray is a contiguous part of the array.

 

// Example 1:

// Input: nums = [1,0,1,0,1], goal = 2
// Output: 4
// Explanation: The 4 subarrays are bolded and underlined below:
// [1,0,1,0,1]
// [1,0,1,0,1]
// [1,0,1,0,1]
// [1,0,1,0,1]

// Example 2:

// Input: nums = [0,0,0,0,0], goal = 0
// Output: 15

 

// Constraints:

//     1 <= nums.length <= 3 * 104
//     nums[i] is either 0 or 1.
//     0 <= goal <= nums.length

// Seen this question in a real interview before?
// 1/4
// Yes
// No
// Accepted
// 211.4K
// Submissions
// 342.1K
// Acceptance Rate
// 61.8%

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        Map<Integer,Integer> prefixmp = new HashMap<>();
        prefixmp.put(0,1);
        int count = 0;
        int ans = 0;
        for(int num : nums){
            count += num;
            if(prefixmp.containsKey(count-goal)){
             
                ans+=prefixmp.get(count-goal);
            }

            prefixmp.put(count,prefixmp.getOrDefault(count,0)+1);
        }
        
        return ans;
    }
}

// 1 0 1 0 1
// 1 1 2 1                  ans = (101) (1010)


// map (num - times)

// 0 - 1
// 1 - 2
// 2 - 2
