# 978. Longest Turbulent Subarray
# Medium
# 1.8K
# 208
# Companies

# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

#     For i <= k < j:
#         arr[k] > arr[k + 1] when k is odd, and
#         arr[k] < arr[k + 1] when k is even.
#     Or, for i <= k < j:
#         arr[k] > arr[k + 1] when k is even, and
#         arr[k] < arr[k + 1] when k is odd.

 

# Example 1:

# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

# Example 2:

# Input: arr = [4,8,12,16]
# Output: 2

# Example 3:

# Input: arr = [100]
# Output: 1

 

# Constraints:

#     1 <= arr.length <= 4 * 104
#     0 <= arr[i] <= 109

# Accepted
# 89K
# Submissions
# 188.5K
# Acceptance Rate
# 47.2%

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        nextNeedGreater = True 

        ans = 1
        temp = 1
        i = 1

        while i < len(arr):
            
            if temp == 1 :
                if arr[i-1] < arr[i]:
                    nextNeedGreater = False
                elif arr[i-1] > arr[i]:
                    nextNeedGreater = True
                else :
                    i+=1
                    continue

                temp+=1

            elif nextNeedGreater and arr[i-1] < arr[i]:
                nextNeedGreater = False
                temp+=1
            
            elif not nextNeedGreater and arr[i-1] > arr[i] :
                nextNeedGreater = True
                temp+=1

            else :
                temp = 1
                continue
            
            ans = max(ans,temp)
            i+=1

        return ans 
            

        