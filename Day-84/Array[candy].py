# 135. Candy
# Hard
# 6.9K
# 500
# Companies

# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

#     Each child must have at least one candy.
#     Children with a higher rating get more candies than their neighbors.

# Return the minimum number of candies you need to have to distribute the candies to the children.

 

# Example 1:

# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# Example 2:

# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.

 

# Constraints:

#     n == ratings.length
#     1 <= n <= 2 * 104
#     0 <= ratings[i] <= 2 * 104

# Accepted
# 394.4K
# S

class Solution:
    def candy(self, ratings: List[int]) -> int:

        ans = [1 for i in range(len(ratings))]

        #left pass
        n = len(ratings)

        for i in range(1,n):
            if ratings[i] > ratings[i-1] :
                ans[i] += ans[i-1]

       
        #right pass

        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1] :
                ans[i] = max(ans[i] , ans[i+1] + 1)

        

        return sum(ans)