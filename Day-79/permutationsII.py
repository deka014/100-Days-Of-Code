# 47. Permutations II
# Medium
# 8K
# 135
# Companies

# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

 

# Constraints:

#     1 <= nums.length <= 8
#     -10 <= nums[i] <= 10

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:


        n = len(nums)
        ans = []
        def rec(index,numset) :

            if index == n :
                ans.append(list(nums))
            
            for i in range(index,n):

                if not nums[i] in numset:
                    nums[index] , nums[i] = nums[i] , nums[index]
                    rec(index+1,set())
                    nums[index] , nums[i] = nums[i] , nums[index]
                    numset.add(nums[i])


        
        rec(0,set())

        return ans