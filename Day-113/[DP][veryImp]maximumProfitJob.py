# 1235. Maximum Profit in Job Scheduling
# Hard
# 6.1K
# 80
# Companies

# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

# You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

# If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

# Example 1:

# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job. 
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

# Example 2:

# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job. 
# Profit obtained 150 = 20 + 70 + 60.

# Example 3:

# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6

 

# Constraints:

#     1 <= startTime.length == endTime.length == profit.length <= 5 * 104
#     1 <= startTime[i] < endTime[i] <= 109
#     1 <= profit[i] <= 104

# Accepted
# 237.5K
# Submissions
# 442.4K
# Acceptance Rate
# 53.7%

from functools import cache
from bisect import bisect_left

class Solution:

    # Bottom-Up
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = sorted(list(zip(startTime, endTime, profit)))
        # dp[i]: the maximum profit if start with job-i, job[i:]
        dp = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            # cur job and next job
            k = bisect_left(jobs, jobs[i][1], key=lambda x: x[0])
            dp[i] = max(dp[i+1], dp[k] + jobs[i][2])
        return dp[0]


# bottom up solution