# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
#         maj = {}
        
#         for i in nums:
#             if not maj.get(i) :
#                 maj[i] = 1
#             else:
                
#                 maj[i] += 1
#             if maj[i] > len(nums)//2:
#                     return i
        # moore algorithm
        count = 0
        el = nums[0]
        for i in range(len(nums)) :
            if count == 0 :
                el = nums[i]
            
            if el == nums[i]:
                count+=1
            else:
                count-=1
        
        return el
                
            
        
