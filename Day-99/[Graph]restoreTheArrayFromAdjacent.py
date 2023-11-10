# 1743. Restore the Array From Adjacent Pairs
# Medium
# 1.4K
# 50
# Companies

# There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

# You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

# It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

# Return the original array nums. If there are multiple solutions, return any of them.

 

# Example 1:

# Input: adjacentPairs = [[2,1],[3,4],[3,2]]
# Output: [1,2,3,4]
# Explanation: This array has all its adjacent pairs in adjacentPairs.
# Notice that adjacentPairs[i] may not be in left-to-right order.

# Example 2:

# Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
# Output: [-2,4,1,-3]
# Explanation: There can be negative numbers.
# Another solution is [-3,1,4,-2], which would also be accepted.

# Example 3:

# Input: adjacentPairs = [[100000,-100000]]
# Output: [100000,-100000]

 

# Constraints:

#     nums.length == n
#     adjacentPairs.length == n - 1
#     adjacentPairs[i].length == 2
#     2 <= n <= 105
#     -105 <= nums[i], ui, vi <= 105
#     There exists some nums that has adjacentPairs as its pairs.

# Accepted
# 60.2K
# Submissions
# 82.7K
# Acceptance Rate
# 72.8%

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        # 1 - 2
        # 2 - 1,3
        # 3 - 4,2
        # 4 - 3

        # 1 2 3 4 

        hashpairs = {}

        ans = []
        
        for i , j in adjacentPairs :
            
            if i in hashpairs :
                hashpairs[i].append(j)
            else :
                hashpairs[i] = [j]

            if j in hashpairs :
                hashpairs[j].append(i)
            else :
                hashpairs[j] = [i]

        visited = set()

        def rec(num):
            ans.append(num)
            visited.add(num)
            for e in hashpairs[num]:
                if not e in visited :
                    rec(e)
                    

        for key in hashpairs :
            if len(hashpairs[key]) == 1 :
                rec(key)
                return ans

