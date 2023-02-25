# Implementing Dijkstra Algorithm
# MediumAccuracy: 50.83%Submissions: 92K+Points: 4
# Lamp
# Don't Miss Out on the Chance to Work with Leading Companies! Visit the GFG Job Fair Now!  

# Given a weighted, undirected and connected graph of V vertices and an adjacency list adj where adj[i] is a list of lists containing two integers where the first integer of each list j denotes there is edge between i and j , second integers corresponds to the weight of that  edge . You are given the source vertex S and You to Find the shortest distance of all the vertex's from the source vertex S. You have to return a list of integers denoting shortest distance between each node and Source vertex S.
 

# Note: The Graph doesn't contain any negative weight cycle.

 

# Example 1:

# Input:
# V = 2
# adj [] = {{{1, 9}}, {{0, 9}}}
# S = 0
# Output:
# 0 9
# Explanation:

# The source vertex is 0. Hence, the shortest 
# distance of node 0 is 0 and the shortest 
# distance from node 1 is 9.

 

# Example 2:

# Input:
# V = 3, E = 3
# adj = {{{1, 1}, {2, 6}}, {{2, 3}, {0, 1}}, {{1, 3}, {0, 6}}}
# S = 2
# Output:
# 4 3 0
# Explanation:

# For nodes 2 to 0, we can follow the path-
# 2-1-0. This has a distance of 1+3 = 4,
# whereas the path 2-0 has a distance of 6. So,
# the Shortest path from 2 to 0 is 4.
# The shortest distance from 0 to 1 is 1 .

class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    
    def dijkstra(self, V, adj, S):
        #code here
        
        def pqSort(q):
            q.sort(key=lambda i : i[0] , reverse = True)
        
        
        parent = [i+1 for i in range(V)]
        distance = [float("inf") for i in range(V)]
        distance[S] = 0
        q = [(0,S)]
        
        while q :
            
            totaldis , node = q.pop()
            
            for curr , dis in adj[node]:
                
                newdis = totaldis + dis 
                
                if newdis < distance[curr] :
                    distance[curr] = newdis
                    parent[curr] = node
                    q.append((newdis,curr))
            
            
            pqSort(q)         
            
        
        return distance
            
            
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends
