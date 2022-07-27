# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

#     For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].

# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

#     For example, the next permutation of arr = [1,2,3] is [1,3,2].
#     Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
#     While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]

# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]

# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr1  = len(nums) - 2
        ptr2  = len(nums) - 1
        
        while ptr1 <= ptr2 : 
            
            if ptr1 ==  -1 :
                return nums.reverse()
            
            if nums[ptr1] < nums[ptr1+1]:
                for i in range(ptr2 , ptr1 , -1):
                    print(i)
                    if nums[i] > nums[ptr1] : 
                        nums[i] , nums[ptr1] = nums[ptr1] , nums[i]
                        nums[ptr1+1:] = nums[ptr1+1:][::-1]
                        return nums
                    
            
            ptr1 -= 1
    

# Intuiton : 

# Step 1: Linearly traverse array from backward such that ith index value of the array is less than (i+1)th index value. Store that index in a variable.

# Step 2: If the index value received from step 1 is less than 0. This means the given input array is the largest lexicographical permutation. Hence, we will reverse the input array to get the minimum or starting permutation. Linearly traverse array from backward. Find an index that has a value greater than the previously found index. Store index is another variable.

# Step 3: Swap values present in indices found in the above two steps.

# Step 4: Reverse array from index+1 where the index is found at step 1 till the end of the array.