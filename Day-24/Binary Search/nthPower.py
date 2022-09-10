# Nth Root of a Number using Binary Search

# Problem Statement: Given two numbers N and M, find the Nth root of M.

# The nth root of a number M is defined as a number X when raised to the power N equals M.

# Example 1:

# Input: N=3 M=27

# Output: 3

# Explanation: The cube root of 27 is 3.

# Example 2:

# Input: N=2 M=16

# Output: 4

# Explanation: The square root of 16 is 4

# Example 3:

# Input: N=5 M=243

# Output: 3

# Explaination: The 5th root of 243 is 3

def findNthRootOfM(n,m):
    # Write your Code here.
    low = 1 
    high = m
    
    while (high - low) > 1e-7:
        mid = (low+high) / 2 
        
        if mid**n <= m :
            low = mid 
        else :
            high = mid 
    
    return round(low,6)
        