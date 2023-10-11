# 2251. Number of Flowers in Full Bloom
# Hard
# 1.3K
# 26
# Companies

# You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.

# Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

 

# Example 1:

# Input: flowers = [[1,6],[3,7],[9,12],[4,13]], poeple = [2,3,7,11]
# Output: [1,2,2,2]
# Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
# For each person, we return the number of flowers in full bloom during their arrival.

# Example 2:

# Input: flowers = [[1,10],[3,3]], poeple = [3,3,2]
# Output: [2,2,1]
# Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
# For each person, we return the number of flowers in full bloom during their arrival.

 

# Constraints:

#     1 <= flowers.length <= 5 * 104
#     flowers[i].length == 2
#     1 <= starti <= endi <= 109
#     1 <= people.length <= 5 * 104
#     1 <= people[i] <= 109

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        start = []
        end = []

        for i in range(len(flowers)):
            start.append(flowers[i][0])
            end.append(flowers[i][1])

        start.sort()
        end.sort()

        ans = []

        for num in people:
            l = 0 
            r = len(flowers) -1 
            blooming = 0
            notblooming = 0
            while l <= r :
                m = l + (r-l)//2 
                
                if start[m] <= num :
                    l = m+1
                else :
                    r = m-1
            
            blooming = l

            l = 0 
            r = len(flowers) -1 

            while l<=r :
                m = l + (r-l)//2 

                if end[m] >= num :
                    r = m-1
                else :
                    l = m+1
        
            notblooming = r+1

            ans.append(blooming - notblooming)

        return ans
            


        




