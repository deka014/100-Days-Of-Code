# 1930. Unique Length-3 Palindromic Subsequences
# Medium
# 1.2K
# 46
# Companies

# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

# A palindrome is a string that reads the same forwards and backwards.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

#     For example, "ace" is a subsequence of "abcde".

 

# Example 1:

# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")

# Example 2:

# Input: s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".

# Example 3:

# Input: s = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba")

 

# Constraints:

#     3 <= s.length <= 105
#     s consists of only lowercase English letters.

# Accepted
# 57.5K
# Submissions
# 92.8K
# Acceptance Rate
# 62.0%

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        

        # x y z -----> here x and z needs to be same

        # 0   1   2   3   4
        
        # b - 0 1 3 5
        # c - 2
        # a - 4 6
        ans = 0

        chrmap = {} # {c : [minindex,maxindex]}

        for i in range(len(s)):
            if not s[i] in chrmap :
                chrmap[s[i]] = [i,None]
            else :
                chrmap[s[i]][1] = i

        for key in chrmap :
            start = chrmap[key][0]
            end = chrmap[key][1]
            if end == None or start+1 == end :
                continue
            visited = set()

            for i in range(start+1,end):
                if s[i] in visited :
                    continue
                ans+=1
                visited.add(s[i])
        
        return ans