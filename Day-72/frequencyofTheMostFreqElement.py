# 1838. Frequency of the Most Frequent Element
# Medium
# 2.7K
# 77
# Companies

# The frequency of an element is the number of times it occurs in an array.

# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.

 

# Example 1:

# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.

# Example 2:

# Input: nums = [1,4,8,13], k = 5
# Output: 2
# Explanation: There are multiple optimal solutions:
# - Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
# - Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
# - Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

# Example 3:

# Input: nums = [3,9,6], k = 2
# Output: 1


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)

        dp = [[0] * n for i in range(n)]

        nums.sort()

        for i in range(n):
            for j in range(i,n):
                dp[i][j] = nums[j] - nums[i]

        
        ans = 0
        ops = k
        for j in range(n):
            temp = 0
            for i in range(j,-1,-1):
                
                if ops < dp[i][j] :
                    break
                else :
                    
                    ops -= dp[i][j]
                    temp+=1
            ops = k
            ans = max(temp,ans)

        return ans


# above n * m solution 

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        #sliding window 

        ans = 1

        i = 0
        j = 0 
        currsum = 0
        winLen = 1

        while j < len(nums):

            currsum += nums[j]

            while nums[j] * (j - i + 1) > currsum + k :
                currsum-=nums[i]
                i+=1

            winLen = j - i + 1
            ans = max(winLen,ans)
            j+=1


        return ans

                
#above nlogn solution
