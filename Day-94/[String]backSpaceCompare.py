# 844. Backspace String Compare
# Easy
# 7.2K
# 329
# Companies

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

 

# Constraints:

#     1 <= s.length, t.length <= 200
#     s and t only contain lowercase letters and '#' characters.

 

# Follow up: Can you solve it in O(n) time and O(1) space?
# Accepted
# 741.1K
# Submissions
# 1.5M
# Acceptance Rate
# 48.9%

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        c1 = ""
        c2 = ""

        i = len(s) -1 
        j = len(t) - 1

        sback = 0

        while i >= 0 :

            if s[i] == "#" :
                sback+=1
            else :
                if sback == 0 :
                    c1+=s[i]
                else :
                    sback-=1
            
            i-=1

        sback = 0 

        while j >= 0 :

            if t[j] == "#" :
                sback+=1
            else :
                if sback == 0 :
                    c2+=t[j]
                else :
                    sback-=1
            
            j-=1
        
        return True if c1 == c2 else False

      