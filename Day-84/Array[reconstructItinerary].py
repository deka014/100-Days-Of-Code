# 332. Reconstruct Itinerary
# Hard
# 5.4K
# 1.8K
# Companies

# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

#     For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

# Example 1:

# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]

# Example 2:

# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

 

# Constraints:

#     1 <= tickets.length <= 300
#     tickets[i].length == 2
#     fromi.length == 3
#     toi.length == 3
#     fromi and toi consist of uppercase English letters.
#     fromi != toi

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        tmap = {}
        visited = {}

        ans = []

        for ticket in tickets :
            arr , dest = ticket

            if arr in  tmap :
                tmap[arr].append(dest)
            else :
                visited[arr] = set([])
                tmap[arr] = [dest]


        for key in tmap :
            tmap[key].sort()

        def rec(source,total,itenlist) :

            if total == len(tickets):
                return itenlist

            if source in tmap:
                for i in range(len(tmap[source])) :
                    
                    if not i in visited[source]:
                        dest = tmap[source][i]
                        itenlist.append(dest)
                        visited[source].add(i)
                        ansfromfuture = rec(dest,total+1,itenlist)
                        if ansfromfuture :
                            return ansfromfuture
                        itenlist.pop()
                        visited[source].remove(i)

            return []
        
        return rec("JFK" , 0 , ["JFK"])


        
        