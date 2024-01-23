# 1239. Maximum Length of a Concatenated String with Unique Characters
# Medium
# 4.2K
# 305
# Companies

# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

# Return the maximum possible length of s.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All the valid concatenations are:
# - ""
# - "un"
# - "iq"
# - "ue"
# - "uniq" ("un" + "iq")
# - "ique" ("iq" + "ue")
# Maximum length is 4.

# Example 2:

# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

# Example 3:

# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
# Explanation: The only string in arr has all 26 characters.

 

# Constraints:

#     1 <= arr.length <= 16
#     1 <= arr[i].length <= 26
#     arr[i] contains only lowercase English letters.

# Accepted
# 254.4K
# Submissions
# 473.7K
# Acceptance Rate
# 53.7%


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        charset = set()

        def commonfound(s):
            #return true if common found else false
            prev = set()
            for l in s:
                if l in charset or l in prev :
                    return True
                prev.add(l)
            return False

        
        def backtrack(index):

            if index == len(arr):
                return len(charset)

            res = 0
            if not commonfound(arr[index]):

                for l in arr[index]:
                    charset.add(l)
                
                res = backtrack(index+1)
                
                for l in arr[index]:
                    charset.remove(l)

            return max(res,backtrack(index+1))
        
        return backtrack(0)



