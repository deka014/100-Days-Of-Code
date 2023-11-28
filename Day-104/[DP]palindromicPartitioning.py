# Palindromic Partitioning
# HardAccuracy: 27.82%Submissions: 126K+Points: 8

# GfG Weekly + You = Perfect Sunday Evenings!
# Register for free now
# banner

# Given a string str, a partitioning of the string is a palindrome partitioning if every sub-string of the partition is a palindrome. Determine the fewest cuts needed for palindrome partitioning of the given string.


# Example 1:

# Input: str = "ababbbabbababa"
# Output: 3
# Explaination: After 3 partitioning substrings 
# are "a", "babbbab", "b", "ababa".

# Example 2:

# Input: str = "aaabba"
# Output: 1
# Explaination: The substrings after 1
# partitioning are "aa" and "abba".


# Your Task:
# You do not need to read input or print anything, Your task is to complete the function palindromicPartition() which takes the string str as the input parameter and returns the minimum number of partitions required.


# Expected Time Complexity: O(n*n) [n is the length of the string str]
# Expected Auxiliary Space: O(n*n)


# Constraints:
# 1 ≤ length of str ≤ 500


#User function Template for python3

class Solution:
    def palindromicPartition(self, string):
        # code here
        
        dp1 = {}
        
        def ifpal(l,r):
            
            
            while l<=r:
                if string[l] != string[r]:
                    return False
                l+=1
                r-=1
            return True
            
        
        def rec(l,r):
            
            
            if l == r or ifpal(l,r-1) :
                return 0
            
            if l in dp1:
                return dp1[l]
                
            temp = r
          
            for i in range(l,r):
                if ifpal(l,i):
                    temp = min(temp,1+rec(i+1,r))
            
            dp1[l] = temp
            
            return temp
                    
        
        return rec(0,len(string))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends