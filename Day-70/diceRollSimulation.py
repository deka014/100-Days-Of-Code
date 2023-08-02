# 1223. Dice Roll Simulation
# Hard
# 871
# 184
# Companies

# A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times.

# Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls. Since the answer may be too large, return it modulo 109 + 7.

# Two sequences are considered different if at least one element differs from each other.

 

# Example 1:

# Input: n = 2, rollMax = [1,1,2,2,2,3]
# Output: 34
# Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.

# Example 2:

# Input: n = 2, rollMax = [1,1,1,1,1,1]
# Output: 30

# Example 3:

# Input: n = 3, rollMax = [1,1,1,2,2,3]
# Output: 181

 

# Constraints:

#     1 <= n <= 5000
#     rollMax.length == 6
#     1 <= rollMax[i] <= 15

# Accepted
# 26.3K
# Submissions
# 54K
# Acceptance Rate
# 48.7%


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        ans = [0]
        def rec(roll,rollMax):
            
            print(roll,rollMax)
            if roll >= 2 :
                ans[0] = ans[0] + 1

            
            for i in range(1,7):

                if rollMax[i-1] > 0 :
                    rollMax[i-1] = rollMax[i-1] - 1
                    rec(roll+1,rollMax)
                    rollMax[i-1] = rollMax[i-1] + 1
        

        rec(0,rollMax)
        return ans[0]




            
