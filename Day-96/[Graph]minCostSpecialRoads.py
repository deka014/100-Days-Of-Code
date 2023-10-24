# 2662. Minimum Cost of a Path With Special Roads
# Medium
# 476
# 71
# Companies

# You are given an array start where start = [startX, startY] represents your initial position (startX, startY) in a 2D space. You are also given the array target where target = [targetX, targetY] represents your target position (targetX, targetY).

# The cost of going from a position (x1, y1) to any other position in the space (x2, y2) is |x2 - x1| + |y2 - y1|.

# There are also some special roads. You are given a 2D array specialRoads where specialRoads[i] = [x1i, y1i, x2i, y2i, costi] indicates that the ith special road can take you from (x1i, y1i) to (x2i, y2i) with a cost equal to costi. You can use each special road any number of times.

# Return the minimum cost required to go from (startX, startY) to (targetX, targetY).

 

# Example 1:

# Input: start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]
# Output: 5
# Explanation: The optimal path from (1,1) to (4,5) is the following:
# - (1,1) -> (1,2). This move has a cost of |1 - 1| + |2 - 1| = 1.
# - (1,2) -> (3,3). This move uses the first special edge, the cost is 2.
# - (3,3) -> (3,4). This move has a cost of |3 - 3| + |4 - 3| = 1.
# - (3,4) -> (4,5). This move uses the second special edge, the cost is 1.
# So the total cost is 1 + 2 + 1 + 1 = 5.
# It can be shown that we cannot achieve a smaller total cost than 5.

# Example 2:

# Input: start = [3,2], target = [5,7], specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
# Output: 7
# Explanation: It is optimal to not use any special edges and go directly from the starting to the ending position with a cost |5 - 3| + |7 - 2| = 7.

 

# Constraints:

#     start.length == target.length == 2
#     1 <= startX <= targetX <= 105
#     1 <= startY <= targetY <= 105
#     1 <= specialRoads.length <= 200
#     specialRoads[i].length == 5
#     startX <= x1i, x2i <= targetX
#     startY <= y1i, y2i <= targetY
#     1 <= costi <= 105

import heapq
class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        currNum = 2
        nodenum = {0 : (start[0],start[1]) , 1 : (target[0] , target[1])}
        spl = {}

        def distance(cord):
            x1,y1,x2,y2 = cord
            return abs(x2-x1) + abs(y2-y1)


        for x1 , y1 , x2 , y2, c in specialRoads :
            
            if not (x1,y1,x2,y2) in spl :
                spl[(x1,y1,x2,y2)] = c
            else :
                if spl[(x1,y1,x2,y2)] > c :
                    spl[(x1,y1,x2,y2)] = c
    

            if not (x1,y1) in nodenum :
                nodenum[currNum] = (x1,y1)
                currNum += 1
                
            if not(x2,y2) in nodenum :
                nodenum[currNum] = (x2,y2)
                currNum+=1
        
        dp = [float("inf") for i in range(currNum) ]
        codedp = {}
        q = [(0,0)]

        while q :
            total,currnode = heapq.heappop(q)

            if currnode == 1:
                return total

            for num in nodenum.keys():
                if num == currnode :
                    continue
                code = nodenum[currnode]+nodenum[num]
                if code in codedp :
                    temp = codedp[code]
                else :
                    temp = distance(code)
                    codedp[code] = temp
                    codedp[nodenum[num]+nodenum[currnode]] = temp
                if code in spl :
                    if spl[code] < temp :
                        temp = spl[code]
                
                if dp[num] > total+temp :     
                    dp[num] = total+temp
                    heapq.heappush(q,(total+temp,num))
        
