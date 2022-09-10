# Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K. The task is to find the element that would be at the k’th position of the final sorted array.
 

# Example 1:

# Input:
# arr1[] = {2, 3, 6, 7, 9}
# arr2[] = {1, 4, 8, 10}
# k = 5
# Output:
# 6
# Explanation:
# The final sorted array would be -
# 1, 2, 3, 4, 6, 7, 8, 9, 10
# The 5th element of this array is 6.

# Example 2:

# Input:
# arr1[] = {100, 112, 256, 349, 770}
# arr2[] = {72, 86, 113, 119, 265, 445, 892}
# k = 7
# Output:
# 256
# Explanation:
# Final sorted array is - 72, 86, 100, 112,
# 113, 119, 256, 265, 349, 445, 770, 892
# 7th element of this array is 256.


# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function kthElement() which takes the arrays arr1[], arr2[], its size N and M respectively and an integer K as inputs and returns the element at the Kth position.


# Expected Time Complexity: O(Log(N) + Log(M))
# Expected Auxiliary Space: O(Log (N))

#User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        
        if len(arr2) < len(arr1) :
            arr1 , arr2  = arr2.copy() , arr1.copy()
            n , m = m , n
        
        # //k - m because what edge case if 2nd array len is less than k
        low = max(0,k-m)
        # k,n beacuase what if k > len(arr1)
        high = min(k,n)
        while low <= high: 
            
            cut1 = (low+high) // 2 
            cut2 = k - cut1
            left1 = float('-inf') if cut1 == 0 else arr1[cut1-1]
            left2 = float('-inf') if cut2 == 0 else arr2[cut2-1]
            
            right1 = float('inf') if cut1 == n else arr1[cut1]
            right2 = float('inf') if cut2 == m else arr2[cut2]
            
            if left1 <= right2 and left2 <= right1 :
                return max(left1,left2)
            elif left1 > right2 :
                high = cut1 - 1
            else :
                low = cut1 + 1
        
        return -1 
                
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends