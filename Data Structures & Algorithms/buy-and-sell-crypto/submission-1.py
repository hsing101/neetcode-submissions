class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i, j = 0, 1
        while j < len(prices):
            m_profit = 0
            if prices[j] > prices[i]:
                r_profit = prices[j] - prices[i]
                profit = max(profit, r_profit)
                j += 1
            else:
                i = j
                j += 1
        return profit




        
