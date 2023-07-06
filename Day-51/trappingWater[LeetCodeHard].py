# 42. Trapping Rain Water
# Hard
# 27.4K
# 377
# Companies

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

 

# Constraints:

#     n == height.length
#     1 <= n <= 2 * 104
#     0 <= height[i] <= 105

# Accepted
# 1.6M
# Submissions
# 2.6M
# Acceptance Rate
# 59.5%



class Solution:
    def trap(self, height) :
        output = 0

        ptr1 = 0
        ptr2 = len(height) - 1
        maxLeft = height[ptr1]
        maxRight = height[ptr2]

        while ptr1<ptr2 :

            if height[ptr1] <= height[ptr2]:
                ptr1+=1
                if maxLeft - height[ptr1] >=0:
                    output+= maxLeft - height[ptr1]

                maxLeft = max(maxLeft,height[ptr1])



            else :
                ptr2-=1
                if maxRight - height[ptr2] >=0:
                    output+= maxRight - height[ptr2]

                maxRight = max(maxRight,height[ptr2])
    
        return output


        