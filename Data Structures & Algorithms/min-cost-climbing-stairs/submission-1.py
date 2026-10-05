class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i  in memo:
                return memo[i]
            if i == 0 or i == 1:
                memo[i] = cost[i]
                return cost[i]
            memo[i] = cost[i] + min(dfs(i - 1), dfs(i - 2))
            return memo[i]
        return min(dfs(len(cost) - 1), dfs(len(cost) - 2))

        