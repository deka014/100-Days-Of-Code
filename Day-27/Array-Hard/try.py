# 76. Minimum Window Substring
# Hard

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.




class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0 
        need = {key:0 for key in t}  
        window = {key:0 for key in t}  
        for i in t:
                need[i]+=1
        
        #substring start and length
        start = 0
        length = float("inf")
        
        #check how many char's number are much in target t string
        valid = 0
        while right < len(s):
            c = s[right]
            
            right +=1
            
            if c in need.keys():
                window[c]+=1
                if window[c] == need[c]:
                    valid +=1
            #windows should shrink        
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                
                d = s[left]
                
                left+=1
                if d in need.keys():                     
                        if window[d] == need[d]:
                            valid-=1
                        window[d] -=1
        minLength = "" if length == int("float") else s[start:start+length]
        return minLength                
