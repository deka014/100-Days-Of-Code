

# 46. Permutations
# Medium
# 17.8K
# 288
# Companies

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:

# Input: nums = [1]
# Output: [[1]]

 

# Constraints:

#     1 <= nums.length <= 6
#     -10 <= nums[i] <= 10
#     All the integers of nums are unique.

# Accepted
# 1.8M
# Submissions
# 2.3M
# Acceptance Rate
# 77.1%
# Seen this question in a real interview before?
# 1/4

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        numset = set()
        n = len(nums)
        ans = []

        # def rec(numset,temp):

        #     if len(temp) == n :
        #         ans.append(list(temp))

        #     for i in range(n):

        #         if not nums[i] in numset :

        #             numset.add(nums[i])
        #             temp.append(nums[i])
        #             rec(numset,temp)
        #             numset.remove(nums[i])
        #             temp.pop()
        
        # rec(numset,[])

        # return ans

        # using no space complexity - O(1)

        def rec2(index):

            if index == n :
                ans.append(list(nums))
            

            for i in range(index,n):

                nums[index] , nums[i] = nums[i] , nums[index] 

                rec2(index+1)

                nums[index] , nums[i] = nums[i] , nums[index]


            

        rec2(0)

        return ans
        