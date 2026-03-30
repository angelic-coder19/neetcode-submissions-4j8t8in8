class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        max_profit = 0
        l, r = 0, 1
        while r < n:
            buy = prices[l]
            sell = prices[r]
            profit = sell - buy

            if profit > max_profit:
                max_profit = profit
            
            if sell < buy:
                l = r

            r += 1 
            

        return max_profit