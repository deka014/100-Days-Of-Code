# 72. Edit Distance
# Hard
# 12.1K
# 140
# Companies

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

#     Insert a character
#     Delete a character
#     Replace a character

 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

 

# Constraints:

#     0 <= word1.length, word2.length <= 500
#     word1 and word2 consist of lowercase English letters.


class Solution:
    def minDistance(self, word1, word2):

        dp = {}
        def helper(i,j):
            

            if i<0 :
                return j+1
            if j<0 :
                return i+1
            
            if (i,j) in dp :
                return dp[(i,j)]
            else:

                if word1[i] == word2[j] : 
                    dp[(i,j)] = 0 + helper(i-1,j-1)
                    return dp[(i,j)]
                
                # replace insert delete
                dp[(i,j)] = min(1+helper(i-1,j-1) , 1+helper(i,j-1) , 1+helper(i-1,j))
                return dp[(i,j)]


        return helper(len(word1)-1 , len(word2) -1)
