
# Time Complexity: O(n) ; Space: O(1) 
class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0
        min_price = 100000

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            profit = prices[i] - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit