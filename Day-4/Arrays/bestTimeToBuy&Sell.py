# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        minPrice = 0
        i = 0
        while i < len(prices) - 1 :
            
            i+=1
            
            if prices[minPrice] > prices[i] :
                minPrice = i
            
            else:
                maxProfit = max(prices[i] - prices[minPrice],maxProfit)
        
        return maxProfit

# Intuiton :
#         1) If the minPrice is greater than the current price, then we chane min price
#         3) If the maxProfit is greater than previous, then we need to change
#         Time Complexity: O(n)