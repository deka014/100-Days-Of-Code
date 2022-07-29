# Given a connected undirected graph. Perform a Depth First Traversal of the graph.
# Note: Use recursive approach to find the DFS traversal of the graph starting from the 0th vertex from left to right according to the graph..


#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        result = []
        visited = {}
        
        def recursive(vertex):
            visited[vertex] = True
            result.append(vertex)
            
            for i in adj[vertex]:
                if not i in visited:
                    recursive(i)
                    
            return result
        
        return recursive(0)




#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        stack = [0]
        result = []
        visited = {}
        print(adj)
        while len(stack) != 0 : 
            print(stack)
            vertex = stack.pop()
            
            visited[vertex] = True
            result.append(vertex)
            
            for i in adj[vertex] : 
                if not i in visited.keys():
                    stack.append(i)
        
        return result
            
                
                    