# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        
        while i <= j :
             
            mid = (i+j) // 2
            
            if nums[mid] == target : 
                return mid
            
            if nums[mid] >= nums[i]:
                if  target >= nums[i] and target <= nums[mid]:
                    j = mid - 1
                else :
                    i = mid + 1
            else : 
                if  target >= nums[mid] and target <= nums[j]:
                    i = mid + 1
                else :
                    j = mid - 1
        
        return -1
                
                

# Intuiton : 

# We divide the array into parts. It is done using two pointers, low and high, 
# and dividing the range between them by 2. This gives the midpoint of the range.
# Check if the target is present in the midpoint, calculated before, of the array.
# If not present, check if the left half of the array is sorted. This implies that 
# binary search can be applied in the left half of the array provided the target lies between the value range.
# Else check into the right half of the array. Repeat the above steps until low <= high. If low > high, indicates we 
# have searched array and target is not present hence return -1. Thus, it makes search operations less as we check range
# first then perform searching in possible ranges which may have target value.