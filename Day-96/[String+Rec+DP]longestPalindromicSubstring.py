# 5. Longest Palindromic Substring
# Medium
# 27.7K
# 1.6K
# Companies

# Given a string s, return the longest
# palindromic
# substring
# in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

 

# Constraints:

#     1 <= s.length <= 1000
#     s consist of only digits and English letters.

# Accepted
# 2.7M
# Submissions
# 8.1M
# Acceptance Rate
# 33.1%

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        dp = [[None] * len(s) for _ in range(len(s))]

        startingIndex = 0
        maxLen = 1
    

        def solve(i,j):
            
            if j<=i:
                return True


            if dp[i][j] != None :
                return dp[i][j]
            
            if s[i] != s[j] :
                dp[i][j] = False
                return False

            dp[i][j] = solve(i+1,j-1)
            
            return dp[i][j]

        for i in range(len(s)):
            for j in range(i+1,len(s)):
                
                if solve(i,j) == True and (j-i+1) > maxLen:
                    startingIndex = i
                    maxLen = (j-i+1)

        
        return s[startingIndex:startingIndex+maxLen]
        

        
        
        