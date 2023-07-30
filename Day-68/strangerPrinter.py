# 664. Strange Printer
# Hard
# 1.7K
# 167
# Companies

# There is a strange printer with the following two special properties:

#     The printer can only print a sequence of the same character each time.
#     At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.

# Given a string s, return the minimum number of turns the printer needed to print it.

 

# Example 1:

# Input: s = "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".

# Example 2:

# Input: s = "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.

 

# Constraints:

#     1 <= s.length <= 100
#     s consists of lowercase English letters.

# Accepted
# 52.5K
# Submissions
# 100.2K
# Acceptance Rate
# 52.4%


class Solution:
    def strangePrinter(self, s: str) -> int:
        
        n = len(s)

        dp = [[-1] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):

                if s[i] == s[j]:
                    dp[i][j] = dp[i][j-1]
                else :
                    dp[i][j] = dp[i][j-1] + 1
                
                for div in range(i,j):
                    dp[i][j] = min(dp[i][j] , dp[i][div] + dp[div+1][j])

        
        return dp[0][n-1]

