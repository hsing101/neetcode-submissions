class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        
        
        memo = {}

        def dp(i, have_coin):
            
            if i >= len(prices):
                return 0 

            key = (i, have_coin)

            if key in memo:
                return memo[key]

            if have_coin:
                memo[key] = max(dp(i + 2, False) + prices[i], dp(i + 1, True))
            else:
                memo[key] = max(dp(i + 1, True) - prices[i], dp(i + 1, False))
            
            return memo[key]
        
        return dp(0, False)


        