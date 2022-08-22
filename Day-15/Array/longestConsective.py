# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

 

# Constraints:

#     0 <= nums.length <= 105
#     -109 <= nums[i] <= 109

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setMap = set(nums)
        longest = 0
        
        for value in setMap:
            temp = 0
            if value - 1 not in setMap:
                temp = 1
            
                while value + temp in setMap:
                    temp+=1
            
            longest = max(temp,longest)
            
        return longest

# Intuiton : check if a smaller consective exist -- if exist then go to next
            
            
            
        
            
        