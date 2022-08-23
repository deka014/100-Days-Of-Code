# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashSet = {}
        longest = 0
        l = 0
        r = 0
        
        while r < len(s):
            
            if s[r] in hashSet :
                l = max(l,hashSet[s[r]] + 1)
                
            hashSet[s[r]] = r
            longest = max(r-l+1 , longest)
            r+=1
            
        return longest