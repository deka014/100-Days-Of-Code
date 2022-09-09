# Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. The stalls are located along a straight line at positions x1,...,xN (0 <= xi <= 1,000,000,000).

# His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, FJ wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?
# Input

# t – the number of test cases, then t test cases follows.
# * Line 1: Two space-separated integers: N and C
# * Lines 2..N+1: Line i+1 contains an integer stall location, xi
# Output

# For each test case output one integer: the largest minimum distance.

# 2
# 4 2
# 5 4 2 1
# 6 4
# 6 7 9 13 15 11

# In test case 1, 
# we only have to allocate rooms to 2 players so we can assign rooms that are first and last which are 1 and 5, so our answer is 5 - 1 = 4.

# In test case 2, 
# there is no way by which we can allocate rooms such that every player will have the 3 or more as its least distance to other players. So the answer is 2 and one possible allocation of rooms is as follows.
#     Player1 = 6
#     Player2 = 9
#     Player3 = 11
#     Player4 = 13 



def chessTournament(positions, n , c):
    positions.sort()
    
    def canPlacePlayer(mid):
        placed = positions[0] 
        count = 1
        for i in range(1,n):
            if positions[i] - placed >= mid:
                placed = positions[i]
                count+=1
            
            if count == c :
                return True 
         
        return False    
            
            
            
    
    low = 1
    high = max(positions) - min(positions)
    result = 0
    
    
    while low<=high: 
        mid = (low+high) // 2 
        if canPlacePlayer(mid):
            low = mid + 1 
            result = mid
        else :
            high = mid - 1
   
    return result

