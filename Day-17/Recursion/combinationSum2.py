# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

 

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        candidates.sort()
        def solve(i,subset,target):
            
            if target == 0 :
                output.append(subset.copy())
            
            if i >= len(candidates) or candidates[i] > target:
                return
            
            prev = -1
            for j in range(i,len(candidates)):
                
                if candidates[j] == prev :
                    continue
                subset.append(candidates[j])
                solve(j+1,subset,target - candidates[j])
                subset.pop()
                prev = candidates[j]
            
        solve(0,[],target)
        return output
                
        
