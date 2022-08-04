# 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = ""
        longest = 1
        
        for i in range(len(s)):
            
            ptr1 , ptr2 = i , i 
            temp = 0
            
            while ptr1 >= 0 and ptr2 < len(s) and s[ptr1] == s[ptr2] :
                if ptr2 - ptr1 + 1 >= longest: 
                    output = s[ptr1 : ptr2 + 1]
                longest = max(ptr2-ptr1 + 1,longest)
                ptr1 -= 1 
                ptr2 += 1
                
                
            
            
            ptr1 , ptr2 = i , i+1
            
            while ptr1 >= 0 and ptr2 < len(s) and s[ptr1] == s[ptr2] :
                if ptr2 - ptr1 + 1 >= longest: 

                    output = s[ptr1 : ptr2 + 1]
                longest = max(ptr2-ptr1 + 1,longest)
                
                ptr1 -= 1 
                ptr2 += 1
                
                
            
                
        
        return output
                
                
# Intuiton : 
#             1) The first while loop check for odd palindrom and expands left and right
#             2) The second while loop check for even palindrom and expans left and right