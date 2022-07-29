# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

# https://leetcode.com/problems/clone-graph/



class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        oldAndNew = {}
        
        def recursion(node):
            
            if node in oldAndNew:
                return oldAndNew[node]
            
            copy = Node(node.val)
            
            oldAndNew[node] = copy
            
            for i in node.neighbors:
                copy.neighbors.append(recursion(i))
            
            return copy
    
        return recursion(node) if node else None