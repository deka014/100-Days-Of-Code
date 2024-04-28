// There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

// You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

// Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

 

// Example 1:

// Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
// Output: [8,12,6,10,10,10]
// Explanation: The tree is shown above.
// We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
// equals 1 + 1 + 2 + 2 + 2 = 8.
// Hence, answer[0] = 8, and so on.

// Example 2:

// Input: n = 1, edges = []
// Output: [0]

// Example 3:

// Input: n = 2, edges = [[1,0]]
// Output: [1,1]

 

// Constraints:

//     1 <= n <= 3 * 104
//     edges.length == n - 1
//     edges[i].length == 2
//     0 <= ai, bi < n
//     ai != bi
//     The given input represents a valid tree.

// Seen this question in a real interview before?
// 1/5
// Yes
// No

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] sumOfDistancesInTree(int n, int[][] edges) {
        Map<Integer,List<Integer>> graph = new HashMap<>();
        int[] countArr = new int[n];
        int[] ans = new int[n];
        if (n==1) return ans;
        for(int[] edge : edges){
            int from = edge[0];
            int to = edge[1];
            graph.computeIfAbsent(from,k->new ArrayList<>()).add(to);
            graph.computeIfAbsent(to,k->new ArrayList<>()).add(from);
        }

        dfsBase(graph,0,0,countArr,0,ans);
        dfs(n,graph,0,0,countArr,ans);
        return ans;
    }

    int dfsBase(Map<Integer,List<Integer>> graph,int currNode,int prev,int[] countArr, int depth,int[] ans){
        int count = 1;
        ans[0] += depth;
        for (int neigh : graph.get(currNode)){
            if (neigh != prev){
                count+= dfsBase(graph,neigh,currNode,countArr,depth+1,ans);
            }
        }
        countArr[currNode] = count;
        return count;
    }

    void dfs(int n ,Map<Integer,List<Integer>> graph,int parentNode,int prevNode,int[] countArr,int[] ans){
        
        for(int neigh : graph.get(parentNode)){
            if (neigh == prevNode){
                continue;
            }
            ans[neigh] = ans[parentNode]-countArr[neigh] +(n-countArr[neigh]);
            dfs(n,graph,neigh,parentNode,countArr,ans);
        }
    }
}