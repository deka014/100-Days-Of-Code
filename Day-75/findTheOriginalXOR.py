# 2433. Find The Original Array of Prefix Xor
# Medium
# 585
# 26
# Companies

# You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

#     pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].

# Note that ^ denotes the bitwise-xor operation.

# It can be proven that the answer is unique.

 

# Example 1:

# Input: pref = [5,2,0,3,1]
# Output: [5,7,2,3,2]
# Explanation: From the array [5,7,2,3,2] we have the following:
# - pref[0] = 5.
# - pref[1] = 5 ^ 7 = 2.
# - pref[2] = 5 ^ 7 ^ 2 = 0.
# - pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
# - pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.

# Example 2:

# Input: pref = [13]
# Output: [13]
# Explanation: We have pref[0] = arr[0] = 13.

 

# Constraints:

#     1 <= pref.length <= 105
#     0 <= pref[i] <= 106

# Accepted
# 39.5K
# Submissions
# 46.2K
# Acceptance Rate
# 85.5%


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        arr = [pref[0]]

        for i in range(1,len(pref)):
            # print(arr[-1],num,arr[-1] ^ num)
            arr.append(pref[i-1] ^ pref[i])
            

        
        return arr
