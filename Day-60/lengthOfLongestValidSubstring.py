# 2781. Length of the Longest Valid Substring
# Hard
# 281
# 3
# Companies

# You are given a string word and an array of strings forbidden.

# A string is called valid if none of its substrings are present in forbidden.

# Return the length of the longest valid substring of the string word.

# A substring is a contiguous sequence of characters in a string, possibly empty.

 

# Example 1:

# Input: word = "cbaaaabc", forbidden = ["aaa","cb"]
# Output: 4
# Explanation: There are 9 valid substrings in word: "c", "b", "a", "ba", "aa", "bc", "baa", "aab", and "aabc". The length of the longest valid substring is 4. 
# It can be shown that all other substrings contain either "aaa" or "cb" as a substring. 

# Example 2:

# Input: word = "leetcode", forbidden = ["de","le","e"]
# Output: 4
# Explanation: There are 11 valid substrings in word: "l", "t", "c", "o", "d", "tc", "co", "od", "tco", "cod", and "tcod". The length of the longest valid substring is 4.
# It can be shown that all other substrings contain either "de", "le", or "e" as a substring. 

 

# Constraints:

#     1 <= word.length <= 105
#     word consists only of lowercase English letters.
#     1 <= forbidden.length <= 105
#     1 <= forbidden[i].length <= 10
#     forbidden[i] consists only of lowercase English letters.

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden_set = set(forbidden)
        res = 0
        right = len(word) - 1
        for left in range(len(word) - 1, -1, -1):
            for k in range(left, min(left + 10, right + 1)):
                if word[left:k+1] in forbidden_set:
                    right = k - 1
                    break
            res = max(res, right - left + 1)
        return res


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        
        ans = 0 
        forbidset = set(forbidden)
        i = 0
        j = 0
        
        def checkforbidden(i,j):
            while i <= j :        
                if word[max(i,j-9):j+1] in forbidset:
                    return True
                i += 1
            return False
        
        while j < len(word):
            
            if checkforbidden(i,j) :
                i = i+1
                j = i
            else :
                ans = max(ans,j-i+1)
                j+=1
        
        return ans

