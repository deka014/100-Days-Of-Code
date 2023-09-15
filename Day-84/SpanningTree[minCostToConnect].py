# 1584. Min Cost to Connect All Points
# Medium
# 4.5K
# 103
# Companies

# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

# Example 1:

# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 

# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.

# Example 2:

# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18

import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def mandistance(x1,y1,x2,y2):
            ans = abs(x1-x2) + abs(y1-y2)
            return ans

        #adj list

        adaj =  {i :[] for i in range(len(points))}

        for i in range(len(points)):
            x1 , y1 = points[i]
            for j in range(i+1,len(points)):
                x2 , y2 = points[j]

                dist = mandistance(x1,y1,x2,y2)

                adaj[i].append([dist,j])
                adaj[j].append([dist,i])


        minhq = [[0,0]]
        visited = set()
        mincost = 0

        while len(visited) < len(points):
            cost , index = heapq.heappop(minhq)

            if index in visited :
                continue
            
            mincost += cost
            visited.add(index)

            for ncost , nindex in adaj[index]:
                
                if nindex not in visited:
                    heapq.heappush(minhq,[ncost,nindex])
                
        
        return mincost








            
            

