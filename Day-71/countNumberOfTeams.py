# 1395. Count Number of Teams
# Medium
# 2.5K
# 182
# Companies

# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:

#     Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
#     A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).

# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

# Example 1:

# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

# Example 2:

# Input: rating = [2,1,3]
# Output: 0
# Explanation: We can't form any team given the conditions.

# Example 3:

# Input: rating = [1,2,3,4]
# Output: 4


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        leftsmaller = [0] * n 
        leftgreater = [0] * n 
        ans = 0

        for i in range(1,n):
            lcount = 0
            rcount = 0
            for j in range(0,i):
                if rating[j] < rating[i] :
                    lcount+=1
                elif rating[j] > rating[i]:
                    rcount+= 1

            leftsmaller[i] = lcount
            leftgreater[i] = rcount

        for i in range(1,n):

            for j in range(0,i):

                if rating[i] > rating[j] : 
                    ans+= leftsmaller[j]
                else : 
                    ans+= leftgreater[j]

        return ans
 