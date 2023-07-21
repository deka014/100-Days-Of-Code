# 739. Daily Temperatures
# Medium
# 11.2K
# 246
# Companies

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]

 

# Constraints:

#     1 <= temperatures.length <= 105
#     30 <= temperatures[i] <= 100

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        N = len(temperatures)
        stackArr = [0]

        ans = [0] * N

        for i in range(1,N): 

            if not stackArr or temperatures[stackArr[-1]] >= temperatures[i]:

                stackArr.append(i)
            
            else : 
                while stackArr and temperatures[i] > temperatures[stackArr[-1]]:
                    valIndex = stackArr.pop()
                    ans[valIndex] = i - valIndex

                stackArr.append(i)
             

                
            
        
        return ans
                
        