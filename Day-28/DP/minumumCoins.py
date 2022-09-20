#important Here greedy will not work beacause the smaller coins can add up to a larger value than existing
#for eg 1,2,5,10,20,50,100,200,500,2000 here it will work because 2 smaller number cant add up to greater than the number
#hence here we used dynamic programming



# Number of Coins
# MediumAccuracy: 47.78%Submissions: 67081Points: 4

# Given a value V and array coins[] of size M, the task is to make the change for V cents, given that you have an infinite supply of each of coins{coins1, coins2, ..., coinsm} valued coins. Find the minimum number of coins to make the change. If not possible to make change then return -1.


# Example 1:

# Input: V = 30, M = 3, coins[] = {25, 10, 5}
# Output: 2
# Explanation: Use one 25 cent coin
# and one 5 cent coin

# Example 2:

# Input: V = 11, M = 4,coins[] = {9, 6, 5, 1} 
# Output: 2 
# Explanation: Use one 6 cent coin
# and one 5 cent coin


# Your Task:  
# You don't need to read input or print anything. Complete the function minCoins() which takes V, M and array coins as input parameters and returns the answer.

# Expected Time Complexity: O(V*M)
# Expected Auxiliary Space: O(V)


def minCoins( coins,V):
        # code here 
        
        hashmap = {}
        mincoin = min(coins)
        hashmap[mincoin] = 1
        coins.sort(reverse = True)
        for i in range(mincoin+1,V+1):
            if i in coins :
                hashmap[i] = 1  
                continue

            
            for j in coins:
                
                if j <= i:
                    if i-j in hashmap:
                        if i in hashmap and hashmap[j] + hashmap[i-j] < hashmap[i]:
                            hashmap[i] = hashmap[j] + hashmap[i-j]
                        elif i not in hashmap :
                            hashmap[i] = hashmap[j] + hashmap[i-j]
                            
        
        
        if V in hashmap :
            return hashmap[V]
        else :
            return -1

# print(minCoins([3, 7, 6, 11, 8],26))