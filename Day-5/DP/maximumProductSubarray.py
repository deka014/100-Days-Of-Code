# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        result = nums[0]
        i = 1
        product1 = nums[0]
        product2 = nums[0]
        
        while i < len(nums) :
            

            temp = max(nums[i],product1 * nums[i] , product2 * nums[i])
            product2 = min(nums[i],product1 * nums[i] , product2 * nums[i])
            product1 = temp
            
            result = max(result,product1)
            
            i+=1
        
        return result
        
# Intution : https://www.youtube.com/watch?v=lXVy6YWFcRM
# The following approach is motivated by Kandane’s algorithm. To know Kadane’s Algorithm follow Kadane’s Algorithm

# The pick point for this problem is that we can get the maximum product from the product of two negative numbers too.

# Following are the steps for the approach:

#     Initially store 0th index value in prod1, prod2 and result.
#     Traverse the array from 1st index. 
#     For each element, update prod1 and prod2.
#     Prod1 is maximum of current element, product of current element and prod1, product of current element and prod2
#     Prod2 is minimum of current element, product of current element and prod1, product of current element and prod2
#     Return maximum of result and prod1
