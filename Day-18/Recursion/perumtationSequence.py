# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

#     "123"
#     "132"
#     "213"
#     "231"
#     "312"
#     "321"

# Given n and k, return the kth permutation sequence.

 

# Example 1:

# Input: n = 3, k = 3
# Output: "213"

# Example 2:

# Input: n = 4, k = 9
# Output: "2314"

# Example 3:

# Input: n = 3, k = 1
# Output: "123"

#Iterative Solution

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [i for i in range(1,n+1)]
        while k>1 : 
            
            pivot = -1 
            for i in range(len(arr) - 2 , -1 , -1):
               
                if  arr[i] < arr[i+1]:
                    pivot = i
                    break
            if pivot > -1 :
                
                for i in range(len(arr)-1,pivot,-1):
                    
                    if arr[i] > arr[pivot] : 
                        
                        arr[i] , arr[pivot] = arr[pivot], arr[i]
                        arr[pivot+1:] = arr[pivot+1:][::-1]
                        break
                
        
            k-=1
        
        return "".join(str(e) for e in arr)
                    
    # do the mathematical solution

                
                        

