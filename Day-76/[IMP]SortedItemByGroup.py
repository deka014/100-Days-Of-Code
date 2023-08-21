# 1203. Sort Items by Groups Respecting Dependencies
# Hard
# 1.6K
# 268
# Companies

# There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

# Return a sorted list of the items such that:

#     The items that belong to the same group are next to each other in the sorted list.
#     There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).

# Return any solution if there is more than one solution and return an empty list if there is no solution.

 

# Example 1:

# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
# Output: [6,3,4,1,5,2,0,7]

# Example 2:

# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
# Output: []
# Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.

 

# Constraints:

#     1 <= m <= n <= 3 * 104
#     group.length == beforeItems.length == n
#     -1 <= group[i] <= m - 1
#     0 <= beforeItems[i].length <= n - 1
#     0 <= beforeItems[i][j] <= n - 1
#     i != beforeItems[i][j]
#     beforeItems[i] does not contain duplicates elements.

from collections import defaultdict , deque
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        itemGroupMap = {}
        beforeOrderMap = defaultdict(list)
        groupOrderMap = defaultdict(list)
        newGroup = m 
        for i in range(n):
            if group[i] == -1 :
                itemGroupMap[i] = newGroup
                newGroup+=1
                continue
            itemGroupMap[i] = group[i]

        for i in range(n):
            for item in beforeItems[i]:
                beforeOrderMap[item].append(i)
       
        for i in range(n):
            if not i in beforeOrderMap :
                continue
            
            for j in beforeOrderMap[i]:
                if itemGroupMap[i] != itemGroupMap[j]:
                    groupOrderMap[itemGroupMap[i]].append(itemGroupMap[j])

        
        def topoSortItems(orderMap,totalItems):
            indegree = [0] * totalItems
            q = deque()
            topo = []
            
            for i in range(totalItems):
                for item in orderMap[i] :
                    indegree[item] += 1 

            for i in range(totalItems):
                if indegree[i] == 0 :
                    q.append(i)

            while q :
        
                el = q.popleft()
                topo.append(el)
            
                for v in orderMap[el]:
                    indegree[v] -= 1

                    if indegree[v] == 0 :
                        q.append(v)
                
            return topo

        beforetopo = topoSortItems(beforeOrderMap,n)
        groupTopo = topoSortItems(groupOrderMap,newGroup)
        

        ansMap  = defaultdict(list)
        ans = []

        for v in beforetopo :
            ansMap[itemGroupMap[v]].append(v)
        
        for v in groupTopo :
            ans += ansMap[v]
            
        return ans if len(ans) == n else []