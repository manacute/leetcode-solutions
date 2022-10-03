class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        minimum, profit = prices[0], 0
        for price in prices:
            minimum = min(minimum, price)
            profit = max(profit, price - minimum)
        
        return profit