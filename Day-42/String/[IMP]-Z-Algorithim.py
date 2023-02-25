

# https://www.youtube.com/watch?v=CpZh4eF8QBw&t=973s
# best explanation 

# The time complexity in naive approach is n2 but it solves in n 

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        newstr = needle + "$" + haystack
        z = [0 for i in range(len(newstr))]

        l , r = 0 , 0 

        for i in range(1,len(newstr)):
            if i > r :
                l , r = i , i
                while r < len(newstr) and newstr[r] == newstr[r-l]:
                    r+=1
                
                r-=1
                
                z[i] = r - l + 1
            
            else:

                if (z[i-l] + i) <= r :
                    z[i] = z[i-l]
                
                else :
                    l = i 

                    while r < len(newstr) and newstr[r] == newstr[r-l]:
                        r+=1
                
                    r-=1
                
                    z[i] = r - l + 1

        ans = -1

        for i in range(len(z)):
            if z[i] == len(needle):
                ans = i
                break

        return -1 if ans== -1 else ans - len(needle) - 1










        