class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        
        memo = {}

        def dp(i, have_coin, balance):
            if i == len(prices) - 1:
                if have_coin:
                    return balance + prices[i]
                else:
                    return balance
            
            if i >= len(prices):
                return balance 

            key = (i, have_coin, balance)

            if key in memo:
                return memo[key]

            if have_coin:
                memo[key] = max(dp(i + 2, False, balance + prices[i]), dp(i + 1, True, balance))
            else:
                memo[key] = max(dp(i + 1, True, balance - prices[i]), dp(i + 1, False, balance))
            
            return memo[key]
        
        return dp(0, False, 0)
                


        