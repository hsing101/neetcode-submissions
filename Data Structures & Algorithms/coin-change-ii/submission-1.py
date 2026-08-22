class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, curr):
            if (i, curr) in memo:
                return memo[(i, curr)]
            if curr > amount or i >= len(coins):
                return 0
            if curr == amount:
                return 1
            if curr < amount:
                memo[(i, curr)] = dfs(i, curr + coins[i]) + dfs(i + 1, curr)
            return memo[(i, curr)]
        return dfs(0, 0)


