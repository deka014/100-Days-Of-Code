# Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
# Note: Unlike 0/1 knapsack, you are allowed to break the item. 

 

# Example 1:

# Input:
# N = 3, W = 50
# values[] = {60,100,120}
# weight[] = {10,20,30}
# Output:
# 240.00
# Explanation:Total maximum value of item
# we can have is 240.00 from the given
# capacity of sack. 

# Example 2:

# Input:
# N = 2, W = 50
# values[] = {60,100}
# weight[] = {10,20}
# Output:
# 160.00
# Explanation:
# Total maximum value of item
# we can have is 160.00 from the given
# capacity of sack.


#User function Template for python3

class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        
        # code here
        Items.sort(key = lambda i : i.value / i.weight , reverse= True )
        result = 0
        for i in Items :
            value = i.value
            weight = i.weight
            if weight <= W :
                result+=value
                W -= weight
            else :
                result+= (value / weight) * W
                W = 0
                break
        
        return result
                
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,Items,n))

# } Driver Code Ends