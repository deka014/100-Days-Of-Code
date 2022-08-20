# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]

# Example 2:

# Input: nums = [1]
# Output: [1]

# Example 3:

# Input: nums = [1,2]
# Output: [1,2]

 

# Constraints:

#     1 <= nums.length <= 5 * 104
#     -109 <= nums[i] <= 109

 

# Follow up: Could you solve the problem in linear time and in O(1) space?


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # moore algorithm extendend
        # there can be a maximum of n/3 major elements thats why 2 count and num
        count1 = 0
        count2 = 0 
        el1 = -1
        el2 = -1
        
        for num in nums:
            if num  == el1:
                count1+=1 
            elif num == el2:
                count2+=1
            elif count1 == 0 :
                el1 = num
                count1 = 1
            elif count2 == 0:
                el2 = num
                count2 = 1
            
            else : 
                count1-=1
                count2-=1
                
        
        majCutoff = len(nums) // 3
        count1 = 0
        count2 = 0
        output = []
        
        for i in nums :
            if i == el1 :
                count1+=1
            elif i == el2 :
                count2+=1
        print(count2, el2, majCutoff)
            
        if count1 > majCutoff :
            output.append(el1)
        if count2 > majCutoff:
            output.append(el2)
                
        
        return output
            
            
            
            
# Intuiton : check striver solution 
# timecomplexity : O(n)
