class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(price - cheapest_price, max_profit)
            if price < cheapest_price:
                cheapest_price = price
        return max_profit