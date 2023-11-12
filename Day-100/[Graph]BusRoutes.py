# 815. Bus Routes
# Hard
# 3.8K
# 105
# Companies

# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

#     For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.

# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

# Example 1:

# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

# Example 2:

# Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# Output: -1

 

# Constraints:

#     1 <= routes.length <= 500.
#     1 <= routes[i].length <= 105
#     All the values of routes[i] are unique.
#     sum(routes[i].length) <= 105
#     0 <= routes[i][j] < 106
#     0 <= source, target < 106

# Accepted
# 167.8K
# Submissions
# 350.8K
# Acceptance Rate
# 47.8%

from collections import deque 

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if target == source :
            return 0
            
        busmap = {}
        junction = set()
        busnum = 0
        visited = set()
        
        for i in range(len(routes)):
            r = routes[i]
            if len(routes) == 1 :
                continue
            
            for stn in r :                
                if stn in busmap :
                    busmap[stn].append(busnum)
                    junction.add(stn)
                else :
                    busmap[stn] = [busnum]

            
            busnum+=1
            
        q = deque()

        for bus in busmap[source]:
            q.append((source,bus,1)) # source , busNo , totalBusTillNow
            visited.add(bus)

        while q :
            source,bus,totalbus = q.popleft()

            if target in set(routes[bus]):
                return totalbus
            
            for stn in routes[bus]:
                if stn in junction :
                    for newbus in busmap[stn] :
                        if not newbus in visited :
                            q.append((stn,newbus,totalbus+1))
                            visited.add(newbus)
        
        return  -1