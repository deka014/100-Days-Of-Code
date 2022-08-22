# Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

# Example 1:

# Input:
# N = 8
# A[] = {15,-2,2,-8,1,7,10,23}
# Output: 5
# Explanation: The largest subarray with
# sum 0 will be -2 2 -8 1 7.

# Your Task:
# You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.

# Expected Time Complexity: O(N*log(N)).
# Expected Auxiliary Space: O(N).

# Constraints:
# 1 <= N <= 105
# -1000 <= A[i] <= 1000, for each valid i


#Your task is to complete this function
#Your should return the required output


class Solution:
    def maxLen(self, n, arr):
        #Code here
        #writing the most optimal solution
        
        hashMap = {}
        longest = 0
        sum = 0
        for i in range(n):
            sum+= arr[i]
            temp = 0
            if sum == 0:
                longest = max(longest,i+1)
            elif sum in hashMap:
                temp = i - hashMap[sum]
                longest = max(longest,temp)
            else :
                hashMap[sum] = i
            
            
        return longest
            
            

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends

# Dry Run: Let us dry run the algorithm for a better understanding

# Input : N = 5, array[] = {1, 2, -2, 4, -4}

# Output : 5

# 1. Initially sum = 0, max = 0

# 2. HashMap<Integer, Integer> h = [ ];

# 3.  => i=0 -> sum=1, sum!=0 so check in hashmap if we’ve seen a subarray with this sum before, in our case hashmap does not contain sum (1), so we add (sum, i) to hashmap.

# h = [[1,0]]

#   => i=1 -> sum=3, sum!=0 so check in hashmap if we’ve seen a subarray with this sum before, in our case hashmap does not contain sum (3), so we add (sum, i) to hashmap.

# h=[[1,0], [3,1]] 

#  => i=2 -> sum=1, sum!=0 so check in hashmap if it contains sum, in our case hashmap contains sum (1)

# Here we can observe that our current sum is seen before which concludes that it’s a zero subarray!

# So we now update our max as maximum(max, 2-0) => max = 2

# h=[[1,0], [3,1]]

# =>  i=3 -> sum=5 , sum!=0 so check in hashmap if it contains sum, in our case hashmap  does not contain sum (5), so we add (sum, i) to hashmap.

# h=[[1,0], [3,1], [5,3]] 

#  => i=4 -> sum=1, sum!=0 so check in hashmap if it contains sum, in our case hashmap contains sum (1)

# Here we can again observe our above discussed case

# So we now update our max as maximum(max, 4-0) => max = maximum(2, 4) = 4

# h=[[1,0], [3,1], [5,3]] 

# 4. Now that we have traversed our whole array, our answer is max = 4

# Subarray = {2, -2, 4, -4}