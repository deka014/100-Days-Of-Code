# 354. Russian Doll Envelopes
# Hard
# 5.4K
# 130
# Companies

# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

# One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

# Note: You cannot rotate an envelope.

 

# Example 1:

# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

# Example 2:

# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1

 

# Constraints:

#     1 <= envelopes.length <= 105
#     envelopes[i].length == 2
#     1 <= wi, hi <= 105

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key = lambda x : (x[0],-x[1]))

        ans = [envelopes[0][1]]

        def lowerbound(val):
            l = 0 
            r = len(ans) -1

            while l <= r:
                m = (l+r) // 2 
                
                if ans[m] < val :
                    l = m+1
                else :
                    r = m-1 
            
            return l

        for i in range(1,len(envelopes)):
            if envelopes[i][1] > ans[-1]:
                ans.append(envelopes[i][1])
            else :
                index = lowerbound(envelopes[i][1])
                ans[index] = envelopes[i][1]

        
        return len(ans)



