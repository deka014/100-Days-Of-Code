# 459. Repeated Substring Pattern
# Easy
# 5.8K
# 461
# Companies

# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.

# Example 2:

# Input: s = "aba"
# Output: false

# Example 3:

# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

 

# Constraints:

#     1 <= s.length <= 104
#     s consists of lowercase English letters.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
         marker = 1
         

         while marker < len(s):
             gotchyaBool = True
             
             if len(s) % marker != 0 :
                 marker+=1
                 continue 
                 
             for i in range(len(s)):
                 
                 if s[i%marker] != s[i]:
                     gotchyaBool = False
                     break
                
                 
             if gotchyaBool == True :
                 return True
             marker+=1
        
         return False
            


        




