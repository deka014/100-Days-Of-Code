# Given a list arr of N integers, print sums of all subsets in it.

 

# Example 1:

# Input:
# N = 2
# arr[] = {2, 3}
# Output:
# 0 2 3 5
# Explanation:
# When no elements is taken then Sum = 0.
# When only 2 is taken then Sum = 2.
# When only 3 is taken then Sum = 3.
# When element 2 and 3 are taken then 
# Sum = 2+3 = 5.

class Solution:
	def subsetSums(self, arr, N):
		# code here
		output = []
		
		def subRec(i,sum):
		    
		    if i == N :
		        output.append(sum)
		        return
		    
		    subRec(i+1,sum)
		    subRec(i+1,sum+arr[i])
		    
		 
		subRec(0,0)
		output.sort()
		return output
		