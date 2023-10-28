# 1220. Count Vowels Permutation
# Hard
# 3K
# 205
# Companies

# Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

#     Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
#     Each vowel 'a' may only be followed by an 'e'.
#     Each vowel 'e' may only be followed by an 'a' or an 'i'.
#     Each vowel 'i' may not be followed by another 'i'.
#     Each vowel 'o' may only be followed by an 'i' or a 'u'.
#     Each vowel 'u' may only be followed by an 'a'.

# Since the answer may be too large, return it modulo 10^9 + 7.

 

# Example 1:

# Input: n = 1
# Output: 5
# Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

# Example 2:

# Input: n = 2
# Output: 10
# Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

# Example 3: 

# Input: n = 5
# Output: 68

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        #rules 
        
        # a - e
        # e - a , i
        # o - i , u
        # u - a
        # i - a , e , o , u 

        rulemap = {
            "a" : ["e"],
            "e" : ["a","i"],
            "o" : ["i" , "u"],
            "u" : ["a"],
            "i" : ["a","e","o","u"]
        }

        def ans(letter,wordlen):
            if wordlen == n : 
                return 1
            
            if (letter,n-wordlen) in dp :
                return dp[letter,n-wordlen]

            totalwords = 0

            for nextletter in rulemap[letter]:
                totalwords += ans(nextletter,wordlen+1)

            dp[(letter,n-wordlen)] = totalwords

            return totalwords
        
        totalwords = 0

        for letter in rulemap.keys():
            totalwords += ans(letter,1)
        
        return totalwords % ((10**9) + 7)


    