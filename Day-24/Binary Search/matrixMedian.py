# Given a matrix of integers A of size N x M in which each row is sorted.

# Find an return the overall median of the matrix A.

# Note: No extra memory is allowed.

# Note: Rows are numbered from top to bottom and columns are numbered from left to right.




# Input Format

# The first and only argument given is the integer matrix A.

# Output Format

# Return the overall median of the matrix A.

# Constraints

# 1 <= N, M <= 10^5
# 1 <= N*M  <= 10^6
# 1 <= A[i] <= 10^9
# N*M is odd

# For Example

# Input 1:
#     A = [   [1, 3, 5],
#             [2, 6, 9],
#             [3, 6, 9]   ]
# Output 1:
#     5
# Explanation 1:
#     A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
#     Median is 5. So, we return 5.

# Input 2:
#     A = [   [5, 17, 100]    ]
# Output 2:
#     17 ``` Matrix=

# ```

def getMedian(matrix):
    # Write your code here.
    def findSmallerOrEqual(target,row):
        low = 0
        high = len(matrix[row]) - 1 
        while low <= high:
            mid = (low + high) // 2 
            if matrix[row][mid] <= target :
                low = mid + 1
            else :
                high = mid - 1
            
        return low
            
        
    
    low = 1
    high = 1e05
    
    while low<=high:
        mid = (low+high) // 2 
        count = 0
        for i in range(len(matrix)):
            count += findSmallerOrEqual(mid,i)
        
        if count <= (len(matrix) * len(matrix[0])) // 2 :
            low = mid + 1 
        else :
            high = mid - 1
    return int(low)  
