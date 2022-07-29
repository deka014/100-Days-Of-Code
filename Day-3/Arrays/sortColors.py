# Given an array nums with n objects colored red, white, or blue, sort them in-place so that 
# objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, 
# respectively.

# You must solve this problem without using the library's sort function.

# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3 pointer approach
        
        low , mid , high  = 0 , 0 , len(nums)-1
        
        while mid <= high :
            
            if nums[mid] == 1 :
                mid += 1
                
            elif nums[mid] == 0 : 
                print(mid)
                nums[low] , nums[mid] = nums[mid] , nums[low]
                low += 1
                mid += 1
            
            else : 
                nums[high] , nums[mid] = nums[mid], nums[high]
                high -= 1
        
        return nums
            

# Intuiton :
#         1) If the mid number is 1, then we need to move the mid pointer to the next element.
#         2) If the mid number is 0, then we need to move the mid and low pointer to the next element.
#         3) If the number is 2, then we need to move the high pointer to the previous element.