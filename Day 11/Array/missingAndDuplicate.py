# #very very important xor approach using xor

# You are given a read only array of n integers from 1 to n.

# Each integer appears exactly once except A which appears twice and B which is missing.

# Return A and B.

# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Note that in your output A should precede B.

# Example:

# Input:[3 1 2 5 3] 

# Output:[3, 4] 

# A = 3, B = 4


# Python3 program to find the repeating
# and missing elements
 
# The output of this function is stored
# at x and y
def getTwoElements(arr, n):
     
    global x, y
    x = 0
    y = 0
     
    # Will hold xor of all elements
    # and numbers from 1 to n
    xor1 = arr[0]
     
    # Get the xor of all array elements
    for i in range(1, n):
        xor1 = xor1 ^ arr[i]
         
    # XOR the previous result with numbers
    # from 1 to n
    for i in range(1, n + 1):
        xor1 = xor1 ^ i
     
    # Will have only single set bit of xor1
    set_bit_no = xor1 & ~(xor1 - 1)
     
    # Now divide elements into two
    # sets by comparing a rightmost set
    # bit of xor1 with the bit at the same
    # position in each element. Also,
    # get XORs of two sets. The two
    # XORs are the output elements.
    # The following two for loops
    # serve the purpose
    for i in range(n):
        if (arr[i] & set_bit_no) != 0:
             
            # arr[i] belongs to first set
            x = x ^ arr[i]
        else:
             
            # arr[i] belongs to second set
            y = y ^ arr[i]
             
    for i in range(1, n + 1):
        if (i & set_bit_no) != 0:
             
            # i belongs to first set
            x = x ^ i
        else:
             
            # i belongs to second set
            y = y ^ i
         
    # x and y hold the desired
    # output elements
     
# Driver code
arr = [ 1, 3, 4, 5, 5, 6, 2 ]
n = len(arr)
     
getTwoElements(arr, n)
 
print("The missing element is", x,
      "and the repeating number is", y)


# https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/
     
