# 44. Wildcard Matching
# Hard
# 7.3K
# 306
# Companies

# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

#     '?' Matches any single character.
#     '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:

# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.

# Example 3:

# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

 

# Constraints:

#     0 <= s.length, p.length <= 2000
#     s contains only lowercase English letters.
#     p contains only lowercase English letters, '?' or '*'.


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def recsol(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                # If we have reached the end of pattern 'p',
                # check if we have also reached the end of the string 's'.
                return i == len(s)

            if p[j] == "*":
                # If the current character in pattern is "*", we have two choices:
                # 1. Skip the "*" and the character that follows it in pattern.
                # 2. Keep the "*" and move to the next character in the string.
                result = recsol(i, j+1) or (i < len(s) and recsol(i+1, j))
            elif i < len(s) and (p[j] == '?' or p[j] == s[i]):
                # If the current characters match (either '?' or the same character),
                # move to the next character in both string and pattern.
                result = recsol(i+1, j+1)
            else:
                result = False

            memo[(i, j)] = result
            return result

        # Start the recursive function call from index 0 of both strings.
        return recsol(0, 0)

