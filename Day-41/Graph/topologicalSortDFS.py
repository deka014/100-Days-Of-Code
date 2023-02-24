# Topological sort
# MediumAccuracy: 56.52%Submissions: 125K+Points: 4
# Lamp
# Don't Miss Out on the Chance to Work with Leading Companies! Visit the GFG Job Fair Now!  

# Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.


# Example 1:

# Input:

# Output:
# 1
# Explanation:
# The output 1 denotes that the order is
# valid. So, if you have, implemented
# your function correctly, then output
# would be 1 for all test cases.
# One possible Topological order for the
# graph is 3, 2, 1, 0.

# Example 2:

# Input:

# Output:
# 1
# Explanation:
# The output 1 denotes that the order is
# valid. So, if you have, implemented
# your function correctly, then output
# would be 1 for all test cases.
# One possible Topological order for the
# graph is 5, 4, 2, 1, 3, 0.

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        stack = []
        visited = {}
        def rec(node):
            
            if node not in visited:
                
                visited[node] = 1
                
                for n in adj[node]:
                    rec(n)
                
                stack.append(node)
                
        for i in range(V):
            if i not in visited:
                rec(i)
        
        stack.reverse()
        return stack
        
        # Code here



#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends