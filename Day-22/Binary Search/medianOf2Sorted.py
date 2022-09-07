# 4. Median of Two Sorted Arrays
# Hard

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums2) < len(nums1) :
            nums1 , nums2 = nums2 , nums1
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        l = 0
        r = n1
        
        while l <= r :
            
            cut1 = (l+r) // 2 
            cut2 = (n1 + n2 + 1) // 2 - cut1
            
            left1 = float("-inf") if cut1 == 0 else nums1[cut1-1]
            left2 = float("-inf") if cut2 == 0 else nums2[cut2-1]
            
            right1 = float("inf") if cut1 == n1 else nums1[cut1]
            right2 = float("inf") if cut2 == n2 else nums2[cut2]
            
            if left1 <= right2 and left2 <= right1 :
                if (n1+n2) % 2 == 0 :
                    return ((max(left1,left2) + min(right1,right2))/2)
                else :
                    return max(left1,left2)
            
            elif left1 > right2 :
                r = cut1 - 1
            
            else :
                l = cut1+1
                
                
        return 0.00    
        
# Intuiton : https://takeuforward.org/data-structure/median-of-two-sorted-arrays-of-different-sizes/


        
        
        
        
        
        
        
        