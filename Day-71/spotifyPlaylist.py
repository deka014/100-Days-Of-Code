# 920. Number of Music Playlists
# Hard
# 1.4K
# 127
# Companies

# Your music player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:

#     Every song is played at least once.
#     A song can only be played again only if k other songs have been played.

# Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: n = 3, goal = 3, k = 1
# Output: 6
# Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].

# Example 2:

# Input: n = 2, goal = 3, k = 0
# Output: 6
# Explanation: There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].

# Example 3:

# Input: n = 2, goal = 3, k = 1
# Output: 2
# Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].

 

# Constraints:

#     0 <= k < n <= goal <= 100

# Accepted
# 35.8K
# Submissions
# 62.9K
# Acceptance Rate
# 56.8%

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp = {}
        def rec(currgoal,oldsongs):
            
           

            if currgoal == 0 and oldsongs == n :
                return 1
            
            if currgoal == 0 or oldsongs > n :
                return 0 
            
            if (currgoal,oldsongs) in dp :
                return dp[(currgoal,oldsongs)]
            #choose new song

            ans = (n-oldsongs) * rec(currgoal - 1 , oldsongs + 1)

            #choose old song
            if oldsongs > k:
                ans += ((oldsongs - k)  * rec(currgoal - 1 , oldsongs))
            
            dp[(currgoal,oldsongs)] = ans % (10 ** 9 + 7)
            return dp[(currgoal,oldsongs)] 

        return rec(goal,0)