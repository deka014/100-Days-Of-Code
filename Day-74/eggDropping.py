# Egg Dropping Puzzle
# MediumAccuracy: 39.64%Submissions: 121K+Points: 4
# Done with this problem? Now use these skills to apply for a job in Job-A-Thon 21!

# You are given N identical eggs and you have access to a K-floored building from 1 to K.

# There exists a floor f where 0 <= f <= K such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break. There are few rules given below. 

#     An egg that survives a fall can be used again.
#     A broken egg must be discarded.
#     The effect of a fall is the same for all eggs.
#     If the egg doesn't break at a certain floor, it will not break at any floor below.
#     If the eggs breaks at a certain floor, it will break at any floor above.

# Return the minimum number of moves that you need to determine with certainty what the value of f is.

# For more description on this problem see wiki page

# Example 1:

# Input:
# N = 1, K = 2
# Output: 2
# Explanation: 
# 1. Drop the egg from floor 1. If it 
#    breaks, we know that f = 0.
# 2. Otherwise, drop the egg from floor 2.
#    If it breaks, we know that f = 1.
# 3. If it does not break, then we know f = 2.
# 4. Hence, we need at minimum 2 moves to
#    determine with certainty what the value of f is.

# Example 2:

# Input:
# N = 2, K = 10
# Output: 4

# Your Task:
# Complete the function eggDrop() which takes two positive integer N and K as input parameters and returns the minimum number of attempts you need in order to find the critical floor.

# Expected Time Complexity : O(N*(K^2))
# Expected Auxiliary Space: O(N*K)

#User function Template for python3

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):
        # code here
        dp = [[-1] * (n+1) for i in range(k + 1)]
        
        def recsol(totalfloors,eggsleft):
            
            if totalfloors == 0 or totalfloors == 1  :
                return totalfloors
                
            if eggsleft == 1 :
                return totalfloors
            
            if dp[totalfloors][eggsleft] != -1 :
                return dp[totalfloors][eggsleft]
                
            minval = float("inf")
            
            for floor in range(1,totalfloors+1):
                notbroken= 1 + recsol(totalfloors-floor,eggsleft)
                broken = 1 + recsol(floor-1,eggsleft-1)
                
                maxval  = max(notbroken , broken)
                minval = min(minval,maxval)
            
            dp[totalfloors][eggsleft] = minval
            
            return minval 
            
        return recsol(k,n)
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
# } Driver Code Ends