# Maximum sum increasing subsequence
# MediumAccuracy: 40.02%Submissions: 129K+Points: 4
# Win Prize worth ₹6000 with Ease. Register for the Easiest Coding Challenge!  

# Given an array of n positive integers. Find the sum of the maximum sum subsequence of the given array such that the integers in the subsequence are sorted in strictly increasing order i.e. a strictly increasing subsequence. 

# Example 1:

# Input: N = 5, arr[] = {1, 101, 2, 3, 100} 
# Output: 106
# Explanation:The maximum sum of a
# increasing sequence is obtained from
# {1, 2, 3, 100}

# Example 2:

# Input: N = 3, arr[] = {1, 2, 3}
# Output: 6
# Explanation:The maximum sum of a
# increasing sequence is obtained from
# {1, 2, 3}


# Your Task:  
# You don't need to read input or print anything. Complete the function maxSumIS() which takes N and array arr as input parameters and returns the maximum value.


# Expected Time Complexity: O(N2)
# Expected Auxiliary Space: O(N)




#User function Template for python3
class Solution:
    def maxSumIS(self, Arr, n):

        # code here
        dp = {}

        def rec(ind, prev):

            if (ind, prev) in dp:
                return dp[(ind, prev)]
            if ind == len(Arr):
                return 0

            takensum = 0

            if Arr[ind] > prev:
                takensum = Arr[ind] + rec(ind + 1, Arr[ind])

            notsum = rec(ind + 1, prev)

            dp[(ind, prev)] = max(takensum, notsum)
            return max(takensum, notsum)

        return rec(0, -1)
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends