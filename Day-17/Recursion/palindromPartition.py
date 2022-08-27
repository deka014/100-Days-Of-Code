# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:

# Input: s = "a"
# Output: [["a"]]

 

# Constraints:

#     1 <= s.length <= 16
#     s contains only lowercase English letters.


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        output = []
        
        def isPalindrome(string):
            i = 0
            j = len(string) - 1
            
            while i < j :
                if string[i] != string[j]:
                    return False
                i+=1
                j-=1
            return True
            
        def solve(i,subset):
            
            if  i == len(s):
                output.append(subset.copy())
            
            temp = ""
            prev = -1
            for j in range(i,len(s)):
                temp+= s[j]
                if not isPalindrome(temp):
                    continue
                subset.append(temp)
                solve(j+1,subset)
                subset.pop()
                
                
            
        solve(0,[])
        
        return output
            
            
            
            
