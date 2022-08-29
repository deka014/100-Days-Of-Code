# Given an undirected graph and an integer M. The task is to determine if the graph can be colored with at most M colors such that no two adjacent vertices of the graph are colored with the same color. Here coloring of a graph means the assignment of colors to all vertices. Print 1 if it is possible to colour vertices and 0 otherwise.

# Example 1:

# Input:
# N = 4
# M = 3
# E = 5
# Edges[] = {(0,1),(1,2),(2,3),(3,0),(0,2)}
# Output: 1
# Explanation: It is possible to colour the
# given graph using 3 colours.

# Example 2:

# Input:
# N = 3
# M = 2
# E = 3
# Edges[] = {(0,1),(1,2),(0,2)}
# Output: 0


#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    #your code here
    
    def isSafe(node,i,color):
        
        for j in range(len(graph[node])):
            if graph[node][j] == 1 :
                if color[j] == i:
                    return False
        return True
        
    def solve(node,color):
        
        if node == V :
            return True
        
        for i in range(k):
            
            if isSafe(node,i,color):
                color[node] = i
                if solve(node+1,color) :
                    return True
                color[node] = -1
            
        return False
    
    
    return solve(0,[-1 for i in range(V)])
        
    
            
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends