# Given a set of N jobs where each jobi has a deadline and profit associated with it.

# Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with job if and only if the job is completed by its deadline.

# Find the number of jobs done and the maximum profit.

# Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.


# Example 1:

# Input:
# N = 4
# Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
# Output:
# 2 60
# Explanation:
# Job1 and Job3 can be done with
# maximum profit of 60 (20+40).

# Example 2:

# Input:
# N = 5
# Jobs = {(1,2,100),(2,1,19),(3,2,27),
#         (4,1,25),(5,1,15)}
# Output:
# 2 127
# Explanation:
# 2 jobs can be done with
# maximum profit of 127 (100+27).

#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        jlist = list(Jobs)
        jlist.sort(key = lambda i : i.profit,reverse = True)
        
        maxDeadline = 0
        for i in jlist :
            if i.deadline > maxDeadline:
                maxDeadline = i.deadline
        
        jseq = [-1 for i in range(maxDeadline)]
        
        total = 0
        count = 0
        for i in jlist:
            pos = i.deadline - 1
            while pos >= 0 and jseq[pos] != -1 :
                pos-=1
            if pos < 0 :
                continue
            else :
                jseq[pos] = i.id
                count+=1
                total += i.profit
                
                
                
        
        return count,total
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends