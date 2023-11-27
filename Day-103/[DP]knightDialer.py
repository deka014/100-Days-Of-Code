# 935. Knight Dialer
# Medium
# 2.8K
# 426
# Companies

# The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

# A chess knight can move as indicated in the chess diagram below:

# We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).

# Given an integer n, return how many distinct phone numbers of length n we can dial.

# You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

# As the answer may be very large, return the answer modulo 109 + 7.

 

# Example 1:

# Input: n = 1
# Output: 10
# Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.

# Example 2:

# Input: n = 2
# Output: 20
# Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]

# Example 3:

# Input: n = 3131
# Output: 136006598
# Explanation: Please take care of the mod.

 

# Constraints:

#     1 <= n <= 5000

# Accepted
# 148.9K
# Sum

class Solution:
    def knightDialer(self, n: int) -> int:
        
        cmap = [[1,1,1],
                [1,1,1],
                [1,1,1],
                [0,1,0]]
        
        dp = {}

        MOD = (10**9) + 7
       
        def rec(x,y,leftjumps):
          
            if x > 3 or x < 0 or y > 2 or y < 0 or cmap[x][y] == 0 :
                return 0
            if leftjumps == 0:
                return 1
            if (x,y,leftjumps) in dp :
                return dp[(x,y,leftjumps)]
            
            temp = 0

            moves = [(2, -1), (2, 1), (-2, -1), (-2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

            for move in moves:
                nx, ny = x + move[0], y + move[1]
                temp += rec(nx, ny, leftjumps - 1) % MOD

            dp[(x,y,leftjumps)] = temp

            return temp 
            
            
        
        ans = 0
        for x in range(0,4):
            for y in range(0,3):

                ans = (ans + rec(x,y,n-1)) % MOD

        return ans 

