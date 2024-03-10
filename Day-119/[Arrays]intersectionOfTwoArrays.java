// 349. Intersection of Two Arrays
// Solved
// Easy
// Topics
// Companies

// Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

// Example 1:

// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2]

// Example 2:

// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [9,4]
// Explanation: [4,9] is also accepted.

 

// Constraints:

//     1 <= nums1.length, nums2.length <= 1000
//     0 <= nums1[i], nums2[i] <= 1000

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {

        Set<Integer> visited = new HashSet<>();
        List<Integer> ansList = new ArrayList<>();
        Arrays.sort(nums2);

        for(int i = 0; i<nums1.length ; i++){
            if (!visited.contains(nums1[i]) && binarysearch(nums1[i],nums2)) {
                visited.add(nums1[i]);
                ansList.add(nums1[i]);
            }
        }

        int[] ans = new int[ansList.size()];
    for (int i = 0; i < ansList.size(); i++) {
        ans[i] = ansList.get(i);
    }

    return ans;
        
    }

    public boolean binarysearch(int num , int[] arr){
        int l = 0;
        int r = arr.length - 1;
        int mid;

        while (l<=r){
            mid = l + ((r-l)/2);

            if (arr[mid] == num){
                return true;
            }

            if (arr[mid] > num){
                r = mid-1;
            }
            else {
                l = mid+1;
            }
        }

        return false;
    }
}