# 567. Permutation in String
# Medium
# 10.1K
# 323
# Companies

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

 

# Constraints:

#     1 <= s1.length, s2.length <= 104
#     s1 and s2 consist of lowercase English letters.

class Solution:
    def checkInclusion(self, s1, s2) :


        if len(s2) < len(s1):
            return False
            
        arr1 = [0] * 26
        arr2 = [0] * 26 

        for i in range(len(s1)):
            arr1[ord(s1[i]) - ord("a")] += 1
            arr2[ord(s2[i]) - ord("a")] += 1

        matches = 0

        for i in range(26):
            if arr1[i] == arr2[i]:
                matches+=1
        
        l = 0 

        for r in range(len(s1) , len(s2)):
            if matches == 26 :
                return True 
            
            index = ord(s2[r]) - ord("a")
            arr2[index] += 1 

            if arr1[index] == arr2[index] :
                matches+=1
            elif arr1[index] + 1 == arr2[index]:
                matches-=1
            
            index = ord(s2[l]) - ord("a")
            arr2[index] -= 1 

            if arr1[index] == arr2[index] :
                matches+=1
            elif arr1[index] - 1 == arr2[index]:
                matches-=1
            
            l+=1
        return matches == 26

        

        
        