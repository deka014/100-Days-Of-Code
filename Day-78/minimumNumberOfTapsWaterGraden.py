# 1326. Minimum Number of Taps to Open to Water a Garden
# Hard
# 2.9K
# 159
# Companies

# There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

# There are n + 1 taps located at points [0, 1, ..., n] in the garden.

# Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

# Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

 

# Example 1:

# Input: n = 5, ranges = [3,4,1,1,0,0]
# Output: 1
# Explanation: The tap at point 0 can cover the interval [-3,3]
# The tap at point 1 can cover the interval [-3,5]
# The tap at point 2 can cover the interval [1,3]
# The tap at point 3 can cover the interval [2,4]
# The tap at point 4 can cover the interval [4,4]
# The tap at point 5 can cover the interval [5,5]
# Opening Only the second tap will water the whole garden [0,5]

# Example 2:

# Input: n = 3, ranges = [0,0,0,0]
# Output: -1
# Explanation: Even if you activate all the four taps you cannot water the whole garden.

 

# Constraints:

#     1 <= n <= 104
#     ranges.length == n + 1
#     0 <= ranges[i] <= 100

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        minR = 0
        maxR = 0
        ans = 0

        while maxR < n : 

            for i in range(n+1):

                if i - ranges[i] <= minR and i+ ranges[i] > maxR :
                    maxR = i + ranges[i]
                
            ans+=1

            if maxR == minR :
                return -1
            
            minR = maxR
        
        return ans

        # tapRange = []

        # for i in range(n+1):
        #     if i - ranges[i] ==  i + ranges[i]:
        #         continue
        #     tapRange.append([i - ranges[i] , i + ranges[i]])

        
        # tapRange.sort(key=lambda x : (x[1],x[0]))


        # monoStack = []
        # prev = None



        # for i in range(len(tapRange)):
            
        #     if tapRange[i][1] != prev :

        #         while monoStack and (tapRange[i][0] <= monoStack[-1] or tapRange[i][0] == 0) :
        #             monoStack.pop()
                
        #         monoStack.append(tapRange[i][0])
            
        #     else :

        #         continue
        
        #     prev = tapRange[i][1]

        # return len(monoStack) if monoStack else -1
