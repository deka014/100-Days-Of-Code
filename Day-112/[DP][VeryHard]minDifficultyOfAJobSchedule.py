# 1335. Minimum Difficulty of a Job Schedule
# Hard
# 3.2K
# 297
# Companies

# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

# You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

# You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

# Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

 

# Example 1:

# Input: jobDifficulty = [6,5,4,3,2,1], d = 2
# Output: 7
# Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
# Second day you can finish the last job, total difficulty = 1.
# The difficulty of the schedule = 6 + 1 = 7 

# Example 2:

# Input: jobDifficulty = [9,9,9], d = 4
# Output: -1
# Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.

# Example 3:

# Input: jobDifficulty = [1,1,1], d = 3
# Output: 3
# Explanation: The schedule is one job per day. total difficulty will be 3.

 

# Constraints:

#     1 <= jobDifficulty.length <= 300
#     0 <= jobDifficulty[i] <= 1000
#     1 <= d <= 10

# Accepted
# 169K
# Submissions
# 284.3K
# Acceptance Rate
# 59.4%
# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Discussion (143)


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        dp = {}
        if d > len(jobDifficulty):
            return -1
            
        def rec(index,d,currmax,lastcut):

            if (lastcut,d) in dp :
                return dp[(lastcut,d)]
            
            if index == len(jobDifficulty):
                if d==0 or d==1:
                    return currmax
                return float("inf")
            if d == 0 :
                return float("inf")

            ans = min(rec(index+1,d,max(currmax,jobDifficulty[index]),lastcut),currmax+rec(index+1,d-1,jobDifficulty[index],index))

            dp[(lastcut,d)] = ans
            return ans
            
        return rec(1,d,jobDifficulty[0],-1) 